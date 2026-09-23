import pgzrun
import time
import random

WIDTH = 600
HEIGHT= 600

game_over = False
game_complete = False 
game_level = 0

items = ["chips","paper","beach","cola","battery"]

items1 = []
animation = []

def draw():
    global items, game_level, game_over, game_complete 
    screen.clear()
    screen.blit("beach .jpg",(0,0))
    
    if game_over == True:    
        display_message("GAME OVER!")
    elif game_complete == True:
        display_message("GOOD JOB")
    
    else:
        for item in items:
            item.draw()
    

def update():
    global items
    if len(items) == 0:
        items = make_items(game_level)
    
    

pgzrun.go()
    

    
    




