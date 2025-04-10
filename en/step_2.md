<h2 class="c-project-heading--task">Ask a question</h2>
--- task ---
Make your character ask how spicy the food is using `.upper()` to format the speaker name like a script.
--- /task ---

<h2 class="c-project-heading--explainer">Is it too spicy?</h2>

In scripts and plays, the speaker’s name is usually written in **capital letters**.  
We can do this in Python using `.upper()` on a string.

For example, `name.upper()` will change `'Zorp'` to `'ZORP'`.

Let’s use that to format your character’s line in the script!

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights: 13
---
# Story starts
print(f'{name} and their friends walk into a space café')
print(f'ROBOT: Today\'s special is {item}!')
print(f'{name.upper()}: How spicy is that?')
--- /code ---
</div>

<div class="c-project-output">
ZORP: How spicy is that?
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

You can also use `.upper()` for other characters in your script if you'd like to expand your story.

</div>
