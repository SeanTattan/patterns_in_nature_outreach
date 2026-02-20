import math
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


# ---------- Phyllotaxis maths ----------

def generate_phyllotaxis(n_points=2000, c=4.0, divergence_deg=137.507764, power=0.5):
    n = np.arange(1, n_points + 1)
    angles = np.deg2rad(n * divergence_deg)
    radius = c * (n ** power)

    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    return x, y


# ---------- App ----------

class PhylloApp:
    def __init__(self, master):
        self.master = master
        master.title('Golden Ratio Phyllotaxis — Generative Art')

        style = ttk.Style()
        style.configure('TLabel', font=('Segoe UI', 11))
        style.configure('TButton', font=('Segoe UI', 11))
        style.configure('TCheckbutton', font=('Segoe UI', 11))
        style.configure('TCombobox', font=('Segoe UI', 11))

        # ----- Parameters (DEFAULT 2000) -----
        self.params = {
            'n_points': tk.IntVar(value=2000),
            'divergence': tk.DoubleVar(value=137.507764),
            'power': tk.DoubleVar(value=0.5),
            'point_size': tk.DoubleVar(value=6.0),
            'alpha': tk.DoubleVar(value=0.8),
            'colormap': tk.StringVar(value='magma'),
            'rotate': tk.DoubleVar(value=0.0),
            'bg_color': tk.StringVar(value='black'),
        }

        self.frame_controls = ttk.Frame(master, width=360)
        self.frame_controls.grid(row=0, column=0, sticky='ns', padx=12, pady=12)

        self.frame_canvas = ttk.Frame(master)
        self.frame_canvas.grid(row=0, column=1, sticky='nsew', padx=12, pady=12)

        master.columnconfigure(1, weight=1)
        master.rowconfigure(0, weight=1)

        self._build_controls()
        self._build_canvas()
        self.render()

    # ---------- Controls ----------

    def _add_scale(self, parent, label, varname, frm, to):
        ttk.Label(parent, text=label).pack(anchor='w', pady=(10, 2))
        scale = ttk.Scale(
            parent,
            variable=self.params[varname],
            from_=frm,
            to=to,
            orient='horizontal'
        )
        scale.pack(fill='x', ipady=6)
        ttk.Label(parent, textvariable=self.params[varname]).pack(anchor='e')

    def _build_controls(self):
        f = self.frame_controls

        ttk.Label(
            f,
            text='Phyllotaxis Parameters',
            font=('Segoe UI', 13, 'bold')
        ).pack(pady=(0, 10))

        self._add_scale(f, 'Points', 'n_points', 100, 2000)
        self._add_scale(f, 'Divergence (deg)', 'divergence', 0.1, 360.0)
        self._add_scale(f, 'Radius power', 'power', 0.1, 1.5)
        self._add_scale(f, 'Point size', 'point_size', 0.1, 20.0)
        self._add_scale(f, 'Opacity', 'alpha', 0.01, 1.0)
        self._add_scale(f, 'Rotation (deg)', 'rotate', -180, 180)

        ttk.Label(f, text='Colormap').pack(anchor='w', pady=(12, 2))
        ttk.Combobox(
            f,
            textvariable=self.params['colormap'],
            values=sorted([
                'magma','viridis','plasma','inferno',
                'cividis','twilight_shifted','copper'
            ]),
            state='readonly'
        ).pack(fill='x')

        ttk.Label(f, text='Background colour').pack(anchor='w', pady=(12, 2))
        ttk.Combobox(
            f,
            textvariable=self.params['bg_color'],
            values=[
                'black','white','navy','midnightblue',
                'darkgreen','purple','maroon','goldenrod'
            ],
            state='readonly'
        ).pack(fill='x')

        ttk.Button(f, text='Render', command=self.render).pack(fill='x', pady=(18, 6))
        ttk.Button(f, text='Save PNG', command=self.save_png).pack(fill='x')

    # ---------- Canvas ----------

    def _build_canvas(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 8), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_canvas)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

    # ---------- Rendering ----------

    def render(self):
        n = min(2000, int(self.params['n_points'].get()))

        c = 4.0  # ← hardcoded scale
        divergence = float(self.params['divergence'].get())
        power = float(self.params['power'].get())
        ps = float(self.params['point_size'].get())
        alpha = float(self.params['alpha'].get())
        cmap = self.params['colormap'].get()
        rotate_deg = float(self.params['rotate'].get())
        bg = self.params['bg_color'].get()

        x, y = generate_phyllotaxis(n, c, divergence, power)

        if abs(rotate_deg) > 1e-6:
            theta = math.radians(rotate_deg)
            x, y = (
                x * math.cos(theta) - y * math.sin(theta),
                x * math.sin(theta) + y * math.cos(theta),
            )

        r = np.sqrt(x*x + y*y)
        colors = plt.cm.get_cmap(cmap)(plt.Normalize(r.min(), r.max())(r))

        self.ax.clear()
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.ax.set_facecolor(bg)
        self.fig.patch.set_facecolor(bg)

        self.ax.scatter(x, y, s=ps, c=colors, alpha=alpha)

        margin = 0.03
        xmin, xmax = x.min(), x.max()
        ymin, ymax = y.min(), y.max()
        dx, dy = xmax - xmin, ymax - ymin
        self.ax.set_xlim(xmin - dx*margin, xmax + dx*margin)
        self.ax.set_ylim(ymin - dy*margin, ymax + dy*margin)

        self.canvas.draw()

    # ---------- Save ----------

    def save_png(self):
        fn = filedialog.asksaveasfilename(
            defaultextension='.png',
            filetypes=[('PNG image','*.png')]
        )
        if not fn:
            return
        bg = self.params['bg_color'].get()
        self.fig.savefig(fn, dpi=300, bbox_inches='tight',
                         pad_inches=0.05, facecolor=bg)
        messagebox.showinfo('Saved', f'Saved image to:\n{fn}')

    def on_close(self):
        plt.close(self.fig)
        self.master.quit()
        self.master.destroy()


# ---------- Run ----------

if __name__ == '__main__':
    root = tk.Tk()
    app = PhylloApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()

