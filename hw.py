import pgzrun

import random


TITLE = "Grab the Strawberries"

WIDTH = 600

HEIGHT = 500

score = 0

game_over = False

'--------------------------------------------------------------------------------------------------------------------------------------------------'

strawberry = Actor('strawberry')

basket = Actor('basket')

strawberry.pos = (100,100)

basket.x = 30
basket.y = 30

def draw():
    screen.blit("pink_wallpaper", (0,0))
    strawberry.draw()
    basket.draw()

def movest():
    strawberry.x = random.randint(50, WIDTH-50)
    strawberry.y = random.randint(50, WIDTH-50)

'--------------------------------------------------------------------------------------------------------------------------------------------------'
def update():
    global score
    if keyboard.up:
        basket.y -= 5
    if keyboard.down:
        basket.y += 5
    if keyboard.left:
        basket.x -= 5
    if keyboard.right:
        basket.x += 5


'--------------------------------------------------------------------------------------------------------------------------------------------------'

movest()

pgzrun.go()