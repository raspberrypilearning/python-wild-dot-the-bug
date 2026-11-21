<h2 class="c-project-heading--task">Voeg Dots poten toe</h2>

\--- task ---

Gebruik de functie `line()` om poten te tekenen die uit Dots lichaam steken.

\--- /task ---

<h2 class="c-project-heading--explainer">Geef Dot poten!</h2>

Nu Dot een lichaam en ogen heeft, is het tijd om het ook poten te geven.

Je kunt de functie `line()` gebruiken om een poot te tekenen door twee punten met elkaar te verbinden.  
Het formaat is: `line(x1, y1, x2, y2)`

Om de poten beter zichtbaar te maken, gebruik je `stroke('black')` om de kleur in te stellen en `stroke_weight(3)` om de lijnen dikker te maken.

Dit moet je toevoegen aan je `draw()`-functie:

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
![Dot met twee ogen en twee schuine zwarte poten](images/step_3.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Probeer poten aan de zijkanten of bovenkant van het lichaam te tekenen<br />
- Gebruik verschillende `stroke_weight()`-waarden om de poten dikker of dunner te maken<br />
- Gebruik `fill()` vóór cirkels, maar `stroke()` vóór lijnen!

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als je de poten niet ziet:<br />

- Zorg ervoor dat de `line()`-aanroepen zich binnen de `draw()`-functie bevinden<br />
- Heb je alle vier de getallen voor elke regel gebruikt?<br />
- Zorg ervoor dat `stroke()` en `stroke_weight()` vóór je lijnen staan

</div>
