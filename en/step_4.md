<h2 class="c-project-heading--task">Escape the apostrophe</h2>
--- task ---
Add a sentence that contains an apostrophe inside speech by using an escape character.
--- /task ---

<h2 class="c-project-heading--explainer">Escaping confusion!</h2>

If you want to use an apostrophe **inside** speech, you can escape it using a backslash `\`.

This tells Python to treat the apostrophe as part of the text, not the end of the string.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 4
line_highlights: 5
---
print("One kid's sandwich had already disappeared.")
print('Another kid yelled, "That\'s mine!"')
--- /code ---
</div>

<div class="c-project-output">
Another kid yelled, "That's mine!"
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Use `\'` inside a string to include an apostrophe without ending it too early.<br />
For example: `'That\'s funny!'` or `'Don\'t touch that!'`

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If you get a *SyntaxError*, check that:<br />
- You used the backslash before the apostrophe<br />
- All your quotes are properly paired

</div>
