import pgzrun
from random import randint
WIDTH = 600
HEIGHT = 500
miceate = 0
game_over = False
cat = Actor("cat")
cat.pos = 100, 100
mouse = Actor("mouse")
mouse.pos = 200, 200
def draw():
    screen.blit("grass", (0, 0))
    mouse.draw()
    cat.draw()
    screen.draw.text("the amount of mice you ate is: " + str(miceate), color="black", topleft=(10, 10))
    if game_over:
        screen.fill("purple")
        screen.draw.text(
            "Time's Up! Your Final Score is: " + str(miceate),
            midtop=(WIDTH / 2, 10),
            fontsize=40,
            color="red"
        )
def place_mouse():
    mouse.x = randint(70, (WIDTH - 70))
    mouse.y = randint(70, (HEIGHT - 70))
def time_up():
    global game_over
    game_over = True
def update():
    global miceate
    if keyboard.left:
        cat.x = cat.x - 2
    if keyboard.right:
        cat.x = cat.x + 2
    if keyboard.up:
        cat.y = cat.y - 2
    if keyboard.down:
        cat.y = cat.y + 2
    mouse_ate = cat.colliderect(mouse)
    if mouse_ate:
        miceate = miceate + 1
        place_mouse() 
clock.schedule(time_up, 60.0)
pgzrun.go()