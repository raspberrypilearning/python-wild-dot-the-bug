<h2 class="c-project-heading--task">Spice symbols</h2>
--- task ---
Show the robot’s spice symbol and multiply it using a variable.
--- /task ---

<h2 class="c-project-heading--explainer">Heat meter</h2>

The robot uses emoji to describe how spicy it is.

We can use `emoji * level` to repeat the emoji. This works because `emoji` is a string, and `level` is a number!

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 13
line_highlights: 14-15
---
print(f'{name.upper()}: How spicy is that?')
print(f'The robot displays {emoji} on it\'s screen.')
print(f'The symbol blinks and changes to {emoji * level}!')
--- /code ---
</div>

<div class="c-project-output">
The robot displays 🌶️ on it's screen.
The symbol blinks and changes to 🌶️🌶️🌶️🌶️🌶️!
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Try making `level` higher or lower to see what happens.

</div>
