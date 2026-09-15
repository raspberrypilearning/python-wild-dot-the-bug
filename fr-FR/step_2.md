<h2 class="c-project-heading--task">Ajouter les yeux de Dot</h2>

\--- task ---

Dessine deux cercles plus petits pour donner des yeux à Dot.

\--- /task ---

<h2 class="c-project-heading--explainer">Est-ce que Dot peut voir ?</h2>

Donnons à Dot l'insecte deux yeux de dessin animé !

Tu peux utiliser `fill('white')` pour changer la couleur, et `circle(x, y, size)` pour dessiner chacun.

Rappelle-toi : les yeux ne sont que des cercles plus petits. Tu peux les placer n'importe où sur le corps de Dot.

Essaie de modifier la position ou la taille pour donner à Dot un air endormi, surpris ou idiot !

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
![Un cercle noir avec deux yeux blancs de dessin animé sur fond vert](images/step_2.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Essaie de rapprocher ou d'écarter les yeux.  
Tu peux même faire un œil plus grand que l'autre !  
Change les chiffres pour créer ton propre style unique.

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si les yeux n'apparaissent pas :<br />

- Assure-toi que `fill('white')` apparaisse **avant** les cercles des yeux<br />
- Vérifie que chaque `cercle()` a 3 nombres : x, y et size<br />

</div>
