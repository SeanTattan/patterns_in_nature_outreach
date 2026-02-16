# Patterns in Nature – Outreach Tools

This repository contains **two interactive visual tools** designed for school outreach events. Both explore patterns in nature using generative visuals: spirals and trees.  

- **Phyllotaxis Spiral (Python)** – Golden-ratio-based sunflower/spiral patterns  
- **Flametree Explorer (R Shiny)** – Interactive fractal tree generator  

---

## Repository Structure

```
patterns-in-nature-outreach/
│
├── phyllotaxis_spiral/       # Python spiral app
│   ├── phyllotaxis_app.py
│   └── requirements.txt
│
├── flametree/               # R Shiny tree app
│   ├── app.R
│   └── install_packages.R
│
├── examples/                 # Example output images
│
└── README.md                 # This file
```

---

## Phyllotaxis Spiral (Python)

Generates golden-ratio phyllotaxis patterns (sunflower spirals) with interactive parameters:  

- Number of points  
- Radius power  
- Divergence angle  
- Point size, opacity, rotation  
- Colormap and background color  

### How to Run

1. Open terminal/command prompt.  
2. Navigate to the app folder:

```bash
cd phyllotaxis_spiral
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python phyllotaxis_app.py
```

You will see an interactive window to adjust parameters and generate the spiral.

---

## Flametree Explorer (R Shiny)

Generates interactive fractal tree patterns (flametrees) with:

- Growth time and number of trees sliders  
- Colour pickers for branches and background  
- Style selection (`plain` or `nativeflora`)  
- Generate and Save PNG buttons  

### How to Run

1. Open R  
2. Navigate to the app folder:

```r
setwd("flametree")
```

3. Install required packages:

```r
source("install_packages.R")
```

4. Launch the Shiny app:

```r
shiny::runApp()
```

A browser window will open with the interactive tree generator.

---

## Examples

Images of outputs can be found in the `examples/` folder

---

## Outreach Context

These tools are designed for **school-level STEM outreach**:

- Explore mathematics and nature patterns visually  
- Interact with generative algorithms in a hands-on way  

---

## Notes

- **Python app**: `tkinter` is required (comes with most Python installs).  
- **R app**: Requires `shiny`, `flametree`, and `colourpicker`. Use `install_packages.R` to set up easily.  
- Both apps are designed for **interactive exploration**, so performance may vary with very high settings.  

