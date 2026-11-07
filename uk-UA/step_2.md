<h2 class="c-project-heading--task">Додайте Горошинці очі👀 </h2>

\--- task ---

Намалюйте два менших кола, щоб дати Горошинці очі.

\--- /task ---

<h2 class="c-project-heading--explainer">Допоможемо Горошинці бачити?</h2>

Додаймо Горошинці два ока!

Ви можете використати `fill('white')`, щоб змінити колір і `circle(x, y, size)`, щоб намалювати їх.

Пам'ятайте: очі - це маленькі кола. Ви можете розмістити їх будь-де, щоб допомогти Горошинці.

Спробуйте змінити положення або розмір, щоб Горошинка виглядала сонною, здивованою або дурнуватою!

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
line_highlights: 12-14
---

    ```
    fill('black')
    circle(200, 200, 100)
    
    fill('white')
    circle(180, 180, 20)
    circle(220, 180, 20)
    ```

run()

\--- /code ---

</div>

<div class="c-project-output">
![A black circle with two white cartoon eyes on a green background](images/step_2.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Поради

Спробуйте розмістити очі ближче або далі один від одного.  
Ви навіть можете зробити одне око більшим за інше!  
Достатньо замінити одне число, щоб створити свою неповторну Горошинку.

</div>

<div class="c-project-callout c-project-callout--debug">

### Налагодження

Якщо очі не з'являються:<br />

- Переконайтеся, що `fill('white')` знаходиться **перед** колами очей<br />
- Перевірте, що кожне `circle()` має 3 числа: x, y та розмір<br />

</div>
