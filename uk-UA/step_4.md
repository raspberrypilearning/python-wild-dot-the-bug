<h2 class="c-project-heading--task">Give Dot some antennae</h2>

\--- task ---

Use the `line()` function to draw two antennae at the top of Dot's head.

\--- /task ---

<h2 class="c-project-heading--explainer">Add extra bug features</h2>

Lots of bugs have wiggly antennae to help them sense the world. Let’s give Dot two fun antennae!

You can use the `line()` function again to draw each one. Start the line near the top of Dot’s head and make it point upward or sideways.

Here’s what to add next:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 21-22
---

    ```
    line(160, 250, 140, 280)
    line(240, 250, 260, 280)
    
    line(185, 150, 175, 120)
    line(215, 150, 225, 120)
    ```

run()

\--- /code ---

</div>

<div class="c-project-output">
![Dot with eyes, legs, and two antennae sticking out](images/step_4.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Try making one antenna longer than the other for a goofy look<br />
- Try slanting them in different directions for more character

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If the antennae don’t show up:<br />

- Double check the start of the line is near Dot’s head<br />
- Make sure you're using `stroke()` and `stroke_weight()`

</div>
