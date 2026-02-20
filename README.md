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

Uses the R package `flametree`: https://flametree.djnavarro.net/ 

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

------------------------------------------------------------------------

# The Golden Ratio & Phyllotaxis -- What Are We Exploring?

## The Golden Ratio

The golden ratio (φ) is an irrational number:

    φ ≈ 1.618033988...

It appears when a line is divided into two parts such that:

    (whole / large part) = (large part / small part)

This ratio appears in:

-   Sunflowers
-   Pinecones
-   Shell spirals


It is closely related to the Fibonacci sequence:

    1, 1, 2, 3, 5, 8, 13, 21, 34, ...

As the numbers grow, the ratio between consecutive Fibonacci numbers
approaches the golden ratio.

------------------------------------------------------------------------

## Phyllotaxis -- The Mathematics of Leaf Arrangement

Phyllotaxis means "leaf arrangement." It describes how plants arrange
leaves, seeds, or petals around a stem.

Many plants grow new seeds at a constant angle, the
**golden angle**.

### The Golden Angle

The golden angle is approximately:

    137.5°

Each new seed is placed: - 137.5° from the previous one\
- Slightly further from the center

This creates extremely efficient packing --- the pattern seen in
sunflowers.

### Why 137.5°?

Simple angles like 90°, 120°, or 180° cause overlapping rows and gaps.

But 137.5° is an irrational fraction of a circle. The points never
perfectly align, resulting in:

-   Even spacing
-   No gaps
-   Maximum packing efficiency

------------------------------------------------------------------------

# Phyllotaxis Spiral (Python)

Each point is placed using:

    angle = n × divergence_angle  
    radius = n^power  

Where: - n = point number
- divergence_angle ≈ 137.5°
- power controls expansion rate

Students can explore: - What happens when the angle changes\
- How density changes with radius power

------------------------------------------------------------------------

# Fractals & Recursion -- How Trees Grow from Simple Mathemtical Principles

The Flametree Explorer demonstrates two powerful mathematical ideas:

-   **Fractals**
-   **Recursion**

These ideas explain how incredibly complex natural structures can grow
from very simple rules.

------------------------------------------------------------------------

## What Is a Fractal?

A fractal is a pattern that:

-   Repeats at different scales
-   Shows self-similarity
-   Often has fine detail at every zoom level

In simple terms:

> A fractal is a shape made of smaller copies of itself.

------------------------------------------------------------------------

## How Recursive Tree Growth Works

A simple recursive tree rule can be:

1.  Draw a branch forward
2.  Split into two smaller branches
3.  Repeat for each smaller branch
4.  Stop when branches become very small

Even though the rule is simple, the final result looks complex and
organic.

This is how:

-   Trees branch
-   Lungs divide into airways
-   Rivers split into streams

Complexity emerges from repetition.

------------------------------------------------------------------------

## Why Fractals Matter

Fractals help explain:

-   Why trees are efficient at capturing sunlight
-   Why blood vessels efficiently deliver oxygen
-   Why river systems efficiently drain landscapes

They maximise:

-   Surface area\
-   Coverage\
-   Distribution efficiency

------------------------------------------------------------------------

# Flametree Explorer (R Shiny)

Features:

-   Growth time and number of trees sliders
-   Colour pickers
-   Style selection
-   Generate and Save PNG

------------------------------------------------------------------------

# Outreach Context

These tools support discussions about:

-   Mathematics in biology
-   Efficiency in natural systems
-   Fibonacci numbers and spirals
-   Fractals and recursion
-   Algorithmic art

They encourage experimentation, observation, and connecting mathematics
to the natural world.


