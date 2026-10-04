<h2 class="c-project-heading--task">Намалюємо тіло для жуків</h2>

\--- task ---

Намалюйте коло, щоб зробити тіло для жучки Горошинки.

\--- /task ---

<h2 class="c-project-heading--explainer">Наш перший крок!</h2>

Це перша поява жучки Горошинки на екрані!

У цьому проєкті ви створите мультяшного жука, використовуючи Python та код з бібліотеки p5. Ти розпочнеш із малювання одного великого кола — тіло Горошинки!

Це код для початку. Він містить функції `setup()` та `draw()`, які p5 використовує для створення вашого ескізу.

Функція `draw()` виконується під час кожного кадру. Зараз ти малюєш лише одну форму - але невдовзі ти додаси більше!

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 9-10
---

from p5 import \*

def setup():
size(400, 400)
background('lightgreen')

def draw():
\# Намалюємо тут Горошинку!
fill('black')
circle(200, 200, 100)

run()

\--- /code ---

</div>

<div class="c-project-output">
![A single black circle on a green background](images/step_1.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Поради

Ви можете поекспериментувати за допомогою значень \`circle()</code>:

- **Перше число** це позиція центру - x
- **Друге число** це позиція центру кругу - y
- **Третє число** – це розмір

Спробуйте замінити розміри чи використати різні кольори в `fill()` як 'purple'`або`'orange'\`!

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо нічого не відбувається: <br />

- Перевірте, чи `circle()` знаходиться всередині функції `draw()`<br />
- Переконайтеся, що `fill()` йде перед `circle()`<br />
- Не забудьте додати `run()` у самому кінці вашого коду!

</div>