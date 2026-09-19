<h2 class="c-project-heading--task">Dessiner le corps de Dot</h2>

\--- task ---

Dessine un cercle pour former le corps de Dot l'insecte.

\--- /task ---

<h2 class="c-project-heading--explainer">Ta première forme !</h2>

Voici la première apparition de Dot l'insecte à l'écran !

Dans ce projet, tu vas créer un insecte de dessin animé en utilisant Python et du code de la bibliothèque p5. Tu commenceras par dessiner un grand cercle — le corps de Dot !

Voici le code de départ pour t'aider à démarrer. Il comprend les fonctions `setup()` et `draw()` que p5 utilise pour construire ton croquis.

La fonction `draw()` s'exécute à chaque image. Pour l'instant, il ne dessine qu'une seule forme, mais tu en ajouteras bientôt d'autres !

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
\# Dessiner Dot ici !
fill('black')
circle(200, 200, 100)

run()

\--- /code ---

</div>

<div class="c-project-output">
![Un cercle noir sur fond vert](images/step_1.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Tu peux expérimenter avec les valeurs de `circle()` :

- Le **premier nombre** est la position X du **centre** du cercle\*\*
- Le **deuxième nombre** est la position Y du **centre** du cercle\*\*
- Le **troisième nombre** est la taille

Essaie de modifier les nombres et d'utiliser différentes couleurs dans `fill()` comme `'purple'` ou `'orange'` !

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si tu ne vois pas le cercle :<br />

- Vérifie que `circle()` se trouve à l'intérieur de la fonction `draw()`<br />
- Assure-toi que `fill()` précède `circle()`<br />
- N'oublie pas d'inclure `run()` à la toute fin de ton fichier !

</div>