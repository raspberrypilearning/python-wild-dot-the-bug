<h2 class="c-project-heading--task">Décore Dot !</h2>

\--- task ---

Utilise les formes que tu aimes pour donner à Dot une touche personnelle.

\--- /task ---

<h2 class="c-project-heading--explainer">Créer ton Dot</h2>

Dot est prêt à découvrir le monde — mais chaque insecte mérite un look unique !

Décorons Dot avec quelques petits extras. Tu pourrais ajouter :

- Un nœud, une couronne ou un chapeau avec `triangle()` ou `rect()`
- Des joues ou taches avec des `circle()`s plus petits
- Cils ou sourcils utilisant `line()`
- Un ami insecte à côté de Dot !

Voici un exemple qui ajoute un nœud rouge sur la tête de Dot :

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
![Dot avec toutes les caractéristiques et un nœud rouge sur le dessus](images/step_6.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

- Veux-tu changer la personnalité de Dot ? Essaie d'ajouter des sourcils !
- Donne à Dot un meilleur ami en utilisant un autre ensemble de formes à proximité.
- Utilise des couleurs comme `'pink'`, `'orange'`, `'skyblue'`, ou des valeurs RGB comme `fill(255, 255, 0)`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Si tes décorations ne s'affichent pas :<br />

- Assure-toi qu'elles viennent **après** le corps de Dot dans le `draw()`<br />
- `run()` devrait être la toute dernière ligne de ton code<br />
- Vérifie que les valeurs x et y sont comprises entre 0 et 400 pour toutes les formes

</div>

<div class="c-project-callout c-project-callout--tip">

### Avis

Il s'agit d'un projet bêta, ce qui signifie qu'il est tout nouveau et pas encore largement disponible. Si tu as testé ce projet individuellement ou avec ton club, n'hésite pas à nous faire part de ton avis.

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
Donner ton avis </a>

</div>
