<h2 class="c-project-heading--task">Draw Dot's body</h2>
--- task ---
Draw a circle to make Dot the Bug's body.
--- /task ---

<h2 class="c-project-heading--explainer">Your first shape!</h2>

This is Dot the Bug's first appearance on screen!

In this project, you’ll create a cartoon bug using Python and code from the p5 library. You’ll start by drawing one big circle — Dot’s body!

Here’s the starter code to get you going. It includes the `setup()` and `draw()` functions that p5 uses to build your sketch.

The `draw()` function runs every frame. Right now it only draws one shape — but you’ll be adding more soon!

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 9-10
---
from p5 import *

def setup():
    size(400, 400)
    background('lightgreen')

def draw():
    # Draw Dot here!
    fill('black')
    circle(200, 200, 100)

run()
--- /code ---
</div>

<div class="c-project-output">
A single black circle appears on a light green background.
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

You can experiment with the `circle()` values:
- The **first number** is the x-position (left to right)
- The **second number** is the y-position (top to bottom)
- The **third number** is the size (diameter)

Try changing the numbers and using different colours in `fill()` like `'purple'` or `'orange'`!

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If you don’t see the circle:<br />
- Check that `circle()` is inside the `draw()` function<br />
- Make sure `fill()` comes before `circle()`<br />
- Don’t forget to include `run()` at the very end of your file!

</div>