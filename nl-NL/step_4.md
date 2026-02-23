<h2 class="c-project-heading--task">Geef Dot wat antennes</h2>

--- task ---

Gebruik de functie `line()` om twee antennes bovenop Dots kop te tekenen.

--- /task ---

<h2 class="c-project-heading--explainer">Voeg extra keverfuncties toe</h2>

Veel insecten hebben beweeglijke antennes waarmee ze de wereld kunnen waarnemen. Laten we Dot twee leuke antennes geven!

Je kunt de functie `line()` opnieuw gebruiken om ze te tekenen. Begin de lijn bovenaan Dots kop en laat deze naar boven of opzij wijzen.

Dit is wat je vervolgens moet toevoegen:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 21-22
---

    line(160, 250, 140, 280)
    line(240, 250, 260, 280)
    
    line(185, 150, 175, 120)
    line(215, 150, 225, 120)

run()

--- /code ---

</div>

<div class="c-project-output">
![Dot met ogen, poten en twee uitstekende antennes](images/step_4.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Probeer eens één antenne langer te maken dan de andere voor een grappig effect<br />
- Probeer ze in verschillende richtingen te kantelen voor meer karakter

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als de antennes niet verschijnen:<br />

- Controleer nogmaals of het begin van de lijn zich in de buurt van Dots kop bevindt<br />
- Zorg ervoor dat je `stroke()` en `stroke_weight()` gebruikt

</div>
