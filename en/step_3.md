<h2 class="c-project-heading--task">Add Dot's legs</h2>

--- task ---

Use the `line()` function to draw legs coming out from Dot's body.

--- /task ---

<h2 class="c-project-heading--explainer">Give Dot some legs!</h2>

Now that Dot has a body and eyes, it’s time to give them some legs.

You can use the `line()` function to draw a leg by connecting two points.  
The format is: `line(x1, y1, x2, y2)`

To make the legs easier to see, use `stroke('black')` to set the colour, and `stroke_weight(3)` to make the lines thicker.

Here’s what to add to your `draw()` function:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 12
line_highlights: 16-19
---

    fill('white')
    circle(180, 180, 20)
    circle(220, 180, 20)

    stroke('black')
    stroke_weight(3)
    line(160, 250, 140, 280)
    line(240, 250, 260, 280)

run()

--- /code ---
</div>

<div class="c-project-output">
![Dot with two eyes and two angled black legs](images/step_3.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Try drawing legs on the sides or top of the body<br />
- Use different `stroke_weight()` values to make legs thicker or thinner<br />
- Use `fill()` before circles, but `stroke()` before lines!

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If you don’t see the legs:<br />
- Make sure the `line()` calls are inside the `draw()` function<br />
- Did you use all four numbers for each line?<br />
- Make sure `stroke()` and `stroke_weight()` are before your lines

</div>
