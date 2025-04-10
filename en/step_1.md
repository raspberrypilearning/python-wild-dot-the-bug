<h2 class="c-project-heading--task">Set the stage</h2>
--- task ---
Print the opening scene of your space café story using the `name` variable.
--- /task ---

<h2 class="c-project-heading--explainer">Welcome to the play!</h2>

You’ve got some starter code that defines the characters and numbers. You can change these at any time.

 📕 Let’s start the story.  📕

You can use f-strings in Python to add variables into your text. You need to place an `f` before the string starts and the variable name needs to be surrounded by `{}`

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 11-12
---
# Variables
name = 'Zorp'
item = 'lava noodles'
emoji = '🌶️'
level = 5
price = 4
quantity = 3
total_price = price * quantity

# Story starts
print(f'{name} and their friends walk into a space café')
print(f'ROBOT: Today\'s special is {item}!')
--- /code ---
</div>

<div class="c-project-output">
Zorp and their friends walk into a space café<br />
ROBOT: Today's special is lava noodles!
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Try changing the alien's name or the food to something fun!<br />
👽 'Glorb' / 'galactic dumplings'<br />
🛸 'Fizzbit' / 'black hole stew'

</div>
