import pgzrun
import random
WIDTH=600
HEIGHT=600
alien=Actor("alien")
alien.pos=(300,300)
hit=""
def draw():
    screen.fill("red")
    alien.draw()
    screen.draw.text(hit,center = (400,10),color = "black",fontsize = 30)
def on_mouse_down(pos):
    global hit
    if alien.collidepoint(pos):
        alien.pos=((random.randint(0,550),random.randint(0,550)))
        hit="good shot"
    else:
        hit="you missed"

pgzrun.go()