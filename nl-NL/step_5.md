<h2 class="c-project-heading--task">Voeg een bek toe met behulp van een boog</h2>

--- task ---

Gebruik de `arc()`-functie om een lachende bek op Dot te tekenen.

--- /task ---

<h2 class="c-project-heading--explainer">Tijd voor een glimlach!</h2>

Dot is bijna klaar, maar er ontbreekt nog één ding: een glimlach!

Je kunt de functie `arc()` gebruiken om een curve te tekenen die op een bek lijkt.  
Zorg ervoor dat je `fill('white')` gebruikt, zodat het opvalt tegen Dots gezicht.

In p5 ziet de functie `arc()` er als volgt uit:  
`arc(x, y, breedte, hoogte, start_hoek, stop_hoek)`

De **start- en stophoeken** bepalen hoeveel van de cirkel getekend wordt.  
De glimlach hieronder begint aan de linkerkant (0°) en eindigt aan de rechterkant (180°) — dat is een halve cirkel!

Omdat p5 werkt met **radialen** en niet met graden, moet je `radians()` gebruiken om de waarden om te zetten.

Dit kun je onder de ogen toevoegen:

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

--- /code ---

</div>

<div class="c-project-output">
![Dot met een lachende witte boog als mond](images/step_5.png)
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Beweeg de boog omhoog of omlaag om Dot hoger of lager te laten glimlachen<br />
- Verander de grootte om Dots glimlach breder, hoger of gekker te maken

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

Als de glimlach niet verschijnt:<br />

- Heb je `fill('white')` gebruikt om de bek zichtbaar te maken?<br />
- Bevinden de x/y-coördinaten van de boog zich onder de ogen?<br />
- Zorg ervoor dat je `radians()` gebruikt met getallen zoals `radians(180)`

</div>