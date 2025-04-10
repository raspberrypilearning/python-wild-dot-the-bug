<h2 class="c-project-heading--task">Add the price and the order</h2>
--- task ---
Use your variables to print the cost and quantity of the order.
--- /task ---

<h2 class="c-project-heading--explainer">Time to place an order</h2>

Let’s add two more lines to your story.

1. The robot should tell the price of the item using the `item` and `price` variables.
2. Your alien should order a certain number of plates using the `quantity` variable, and use `.upper()` to format the speaker’s name like a script.

The variables in each f-string are placed inside curly braces `{}`. Python will swap those out with the actual values.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 15
line_highlights: 16-17
---
print(f'The symbol blinks and changes to {emoji * level}!')
print(f'ROBOT: Each plate of {item} costs {price} credits.')
print(f'{name.upper()}: I\'ll have {quantity}')
--- /code ---
</div>

<div class="c-project-output">
ROBOT: Each plate of lava noodles costs 4 credits.<br />
ZORP: I'll have 3
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

You can change the name at the top of your file, and `.upper()` will always show it like a script character!

</div>
