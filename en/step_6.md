<h2 class="c-project-heading--task">Decorate Dot!</h2>

--- task ---

Use any shapes you like to give Dot a personal touch.

--- /task ---

<h2 class="c-project-heading--explainer">Make Dot your own</h2>

Dot is ready to meet the world — but every bug deserves their own unique look!

Let’s decorate Dot with some extras. You could add:

- A bow, crown, or hat with `triangle()` or `rect()`
- Cheeks or spots with smaller `circle()`s
- Eyelashes or eyebrows using `line()`
- A bug friend next to Dot!

Here’s an example that adds a red bow on Dot’s head:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 24
line_highlights: 27-29
---

    fill('white')
    arc(200, 215, 40, 20, radians(0), radians(180))

    fill('red')
    triangle(195, 140, 185, 130, 195, 130)
    triangle(205, 140, 215, 130, 205, 130)

run()

--- /code ---
</div>

<div class="c-project-output">
![Dot with all features and a red bow on top](images/step_6.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Want to change Dot’s personality? Try adding eyebrows!
- Give Dot a best friend using another set of shapes nearby.
- Use colours like `'pink'`, `'orange'`, `'skyblue'`, or RGB values like `fill(255, 255, 0)`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If your decorations don’t show up:<br />
- Make sure they come **after** Dot’s body in the `draw()`<br />
- `run()` should be the very last line of your code<br />
- Check that the x and y values are between 0 and 400 for all shapes

</div>

<div class="c-project-callout c-project-callout--tip">

### Feedback

This is a beta projects, which means it is brand new and not widely available. If you've tested this project on your own or with your club, let us know what you think.

<a href="https://form.raspberrypi.org/4874054?tfa_6933=python-wild-dot-the-bug" style="
  display: inline-block;
  padding: 10px 20px;
  border: 2px solid black;
  border-radius: 999px;
  font-weight: bold;
  font-size: 16px;
  background-color: white;
  color: black;
  text-align: center;
  text-decoration: none;
  transition: background-color 0.2s;
" onmouseover="this.style.backgroundColor='#f0f0f0';" onmouseout="this.style.backgroundColor='white';">
  Give feedback
</a>
</div>
