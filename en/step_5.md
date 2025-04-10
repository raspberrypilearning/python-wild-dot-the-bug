<h2 class="c-project-heading--task">Add a mouth using an arc</h2>
--- task ---
Use the `arc()` function to draw a smiling mouth on Dot.
--- /task ---

<h2 class="c-project-heading--explainer">Time for a smile!</h2>

Dot is almost done, but there’s one thing missing: a smile!

You can use the `arc()` function to draw a curve that looks like a mouth.  
Make sure you use `fill('white')` so it stands out from Dot’s face.

In p5, the `arc()` function looks like this:  
`arc(x, y, width, height, start_angle, stop_angle)`

Use `radians()` to convert degrees to angles that p5 understands.

Here’s what to add below the eyes:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 12
line_highlights: 23
---
    fill('white')
    circle(180, 180, 20)
    circle(220, 180, 20)

    stroke('black')
    stroke_weight(3)
    line(160, 250, 140, 280)
    line(240, 250, 260, 280)
    line(185, 150, 175, 120)
    line(215, 150, 225, 120)

    fill('white')
    arc(200, 215, 40, 20, radians(0), radians(180))

run()
--- /code ---
</div>

<div class="c-project-output">
Dot now has a bright white smile!
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Move the arc up or down to make Dot smile higher or lower<br />
- Change the size to make Dot’s smile wider, taller, or goofier

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If the smile doesn’t appear:<br />
- Did you use `fill('white')` to make the mouth visible?<br />
- Are the arc’s x/y coordinates under the eyes?<br />
- Make sure to use `radians()` with numbers like `radians(180)`

</div>
