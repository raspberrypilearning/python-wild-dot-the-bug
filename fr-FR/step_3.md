<h2 class="c-project-heading--task">Ajouter les jambes de Dot</h2>

\--- task ---

Utilise la fonction `line()` pour dessiner des jambes sortant du corps de Dot.

\--- /task ---

<h2 class="c-project-heading--explainer">Donner des jambes à Dot !</h2>

Maintenant que Dot a un corps et des yeux, il est temps de lui donner des jambes.

Tu peux utiliser la fonction `line()` pour dessiner une jambe en reliant deux points.  
Le format est : `line(x1, y1, x2, y2)`

Pour rendre les jambes plus faciles à voir, utilise `stroke('black')` pour définir la couleur et `stroke_weight(3)` pour épaissir les lignes.

Voici ce qu'il faut ajouter à ta fonction `draw()`:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 12
line_highlights: 16-19
---

    ```
    fill('white')
    circle(180, 180, 20)
    circle(220, 180, 20)
    
    stroke('black')
    stroke_weight(3)
    line(160, 250, 140, 280)
    line(240, 250, 260, 280)
    ```

run()

\--- /code ---

</div>

<div class="c-project-output">
![Dot avec deux yeux et deux pattes noires anguleuses](images/step_3.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

- Essaie de dessiner des jambes sur les côtés ou sur le dessus du corps<br />
- Utilise différentes valeurs de `stroke_weight()` pour rendre les jambes plus épaisses ou plus fines<br />
- Utilise `fill()` avant les cercles, mais `stroke()` avant les lignes !

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si tu ne vois pas les jambes :<br />

- Assure-toi que les appels `line()` sont à l'intérieur de la fonction `draw()`<br />
- As-tu utilisé les quatre chiffres pour chaque ligne ?<br />
- Assure-toi que `stroke()` et `stroke_weight()` sont avant tes lignes

</div>
