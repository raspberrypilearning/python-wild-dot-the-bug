<h2 class="c-project-heading--task">Ajouter une bouche en utilisant un arc</h2>

\--- task ---

Utilise la fonction `arc()` pour dessiner une bouche souriante sur Dot.

\--- /task ---

<h2 class="c-project-heading--explainer">Il est temps de sourire !</h2>

Dot est presque terminé, mais il manque une chose : un sourire !

Tu peux utiliser la fonction `arc()` pour dessiner une courbe qui ressemble à une bouche.  
Assure-toi d'utiliser `fill('white')` pour qu'il se distingue du visage de Dot.

Dans p5, la fonction `arc()` ressemble à ceci :  
`arc(x, y, width, height, start_angle, stop_angle)`

Les **angles de départ et d'arrêt** déterminent la portion du cercle qui est dessinée.  
Le sourire ci-dessous commence à gauche (0°) et se termine à droite (180°) — c'est un demi-cercle !

Étant donné que p5 fonctionne en **radians** et non en degrés, tu devras utiliser `radians()` pour convertir les valeurs.

Voici ce qu'il faut ajouter sous les yeux :

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 24-25
---

    ```
    line(185, 150, 175, 120)
    line(215, 150, 225, 120)
    
    fill('white')
    arc(200, 215, 40, 20, radians(0), radians(180))
    ```

run()

\--- /code ---

</div>

<div class="c-project-output">
![Dot avec un arc blanc souriant en guise de bouche](images/step_5.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

- Déplace l'arc vers le haut ou vers le bas pour que le sourire de Dot soit plus grand ou plus petit<br />
- Modifie la taille pour rendre le sourire de Dot plus large, plus haut ou plus rigolo

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si le sourire n'apparaît pas :<br />

- As-tu utilisé `fill('white')` pour rendre la bouche visible ?<br />
- Les coordonnées x/y de l'arc sont-elles sous les yeux ?<br />
- Assure-toi d'utiliser `radians()` avec des nombres comme `radians(180)`

</div>