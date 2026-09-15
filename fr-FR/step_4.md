<h2 class="c-project-heading--task">Donner des antennes à Dot</h2>

\--- task ---

Utilise la fonction `line()` pour dessiner deux antennes sur le dessus de la tête de Dot.

\--- /task ---

<h2 class="c-project-heading--explainer">Ajouter des fonctionnalités supplémentaires à l'insecte</h2>

De nombreux insectes ont des antennes ondulantes pour les aider à sentir le monde. Donnons à Dot deux antennes amusantes !

Tu peux utiliser à nouveau la fonction `line()` pour dessiner chacune d'elles. Commence la ligne près du haut de la tête de Dot et fais-la pointer vers le haut ou vers le haut.

Voici ce qu'il faut ajouter ensuite :

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 21-22
---

    ```
    line(160, 250, 140, 280)
    line(240, 250, 260, 280)
    
    line(185, 150, 175, 120)
    line(215, 150, 225, 120)
    ```

run()

\--- /code ---

</div>

<div class="c-project-output">
![Dot avec des yeux, des pattes et deux antennes qui dépassent](images/step_4.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

- Essaie de faire une antenne plus longue que l'autre pour un look rigolo<br />
- Essaie de les incliner dans différentes directions pour plus de caractères

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si les antennes ne s'affichent pas :<br />

- Vérifie que le début de la ligne se trouve bien près de la tête de Dot<br />
- Assure-toi d'utiliser `stroke()` et `stroke_weight()`

</div>
