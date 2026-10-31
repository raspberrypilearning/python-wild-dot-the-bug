<h2 class="c-project-heading--task">Прикрасьте Горошинку!</h2>

\--- task ---

Використовуйте будь-які форми, які вам подобаються, щоб надати Горошинці своєї особисті.

\--- /task ---

<h2 class="c-project-heading--explainer">Удоскональте Горошинку</h2>

Горошинка майже готова зустріти світ — але всі жуки заслуговують на свій унікальний стиль!

Додамо трохи деталей для Горошинки. Ви можете додати:

- Бантик, корону чи капелюх за допомогою `triangle()` or `rect()`
- Щічки чи ластовиння за допомогою менших `circle()`
- Вії або брови за допомогою `line()`
- Подругу для Горошинки!

Ось приклад, який додає червоний бант на голову Горошинки:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 24
line_highlights: 27-29
---

    ```
    fill('white')
    arc(200, 215, 40, 20, radians(0), radians(180))
    
    fill('red')
    triangle(195, 140, 185, 130, 195, 130)
    triangle(205, 140, 215, 130, 205, 130)
    ```

run()

\--- /code ---

</div>

<div class="c-project-output">
![Dot with all features and a red bow on top](images/step_6.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Поради

- Хочеш додати більше емоцій? Спробуй погратись з бровами!
- Додайте Горошинці найкращу подругу, використовуючи інший набір фігурок поруч.
- Використовуйте кольори типу «pink», «orange», «skyblue» або значення RGB, такі як `fill(255, 255, 0)`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо ваші удосконалення не відображаються:<br />

- Переконайтеся, що вони розташовуються **після** тіла Горошинки у `draw()`<br />
- `run()` повинен бути останнім рядком вашого коду<br />
- Перевірте, чи значення x та y знаходяться в діапазоні від 0 до 400 для всіх фігур

</div>

<div class="c-project-callout c-project-callout--tip">

### Зворотний зв’язок

Це бета-проект, а це означає, що він абсолютно новий і не є широкодоступним. Якщо ви тестували цей проєкт самостійно або зі своїм клубом, поділіться своєю думкою.

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
Give feedback </a>

</div>
