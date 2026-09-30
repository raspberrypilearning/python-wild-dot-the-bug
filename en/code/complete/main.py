from p5 import *

def setup():
    size(400, 400)
    background('lightgreen')

def draw():
    # Draw Dot here!
    fill('black')
    circle(200, 200, 100)

    fill('white')
    circle(180, 180, 20)
    circle(220, 180, 20)

    stroke('black')
    stroke_weight(3)
    line(160, 250, 140, 280)
    line(240, 250, 260, 280)

    line(185, 150, 175, 120)
    line(215, 150, 225, 120)

    fill('white')
    arc(200, 215, 40, 20, radians(0), radians(180))

    fill('red')
    triangle(195, 140, 185, 130, 195, 130)
    triangle(205, 140, 215, 130, 205, 130)

run()
