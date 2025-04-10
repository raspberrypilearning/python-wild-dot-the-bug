<h2 class="c-project-heading--task">Print the final receipt</h2>
--- task ---
Make the robot print a very spicy receipt!
--- /task ---

<h2 class="c-project-heading--explainer">Spicy receipt</h2>

Use all your variables together to show just how spicy the order really was.

This time, we’re using:  
- `emoji * level * total_price`  
This means the emoji will be repeated `level` times per dish, multiplied by how many dishes were ordered.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
---
print('The robot prints an odd receipt:')
print(emoji * level * total_price)
--- /code ---
</div>

<div class="c-project-output">
The robot prints an odd receipt:<br />
🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Try using a different emoji for the receipt or make your own twist by using `emoji * (level + quantity)` or similar.

</div>
