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
    screen.blit("beach",(0,0))
    
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
    
    
def make_items(number_of_extra_items):
    item_to_be_created = get_option_to_create(number_of_extra_items)
    new_item = create_item(item_to_be_created )
    layout_item(new_item)
    animate_items(new_item)
    return new_item


def get_option_to_create(number_of_extra_items):
    item_to_be_created = ["paper"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(items)
        item_to_be_created.append(random_option)
    return item_to_be_created

        
    

def create_item(item_to_be_created):
    new_items = []
    for option in item_to_be_created:
        item = Actor(option + "img")
        new_items.append(item)
    return new_items
        
        
         
def layout_items(items_layout):
    number_of_gaps = len(items_layout) +1
    gap_size = WIDTH /  number_of_gaps
    random.shuffle(items_layout)
    for index, item in enumerate(item_to_layout):
        new_x_pos = (index +1) * gap_size
        item.x = new_x_pos
        
        
def animate_items(items_to_animate):
    global animations 
    for item in items_to_animate:
        duration = START_speed - game_level
        item.anchor = ("center","bottom")
        animation = animate(item, duration = duration,on_finished = handle_game_over, y = height)
        animations.append(animation)
        

def handle_game_over():
    global game_level, animations, items1, game_complete
    stop_animation(animations)
    if current_level == final_level:
        game_complete = True
        
    else:
        game_level =+ 1
        items=[]
        animation=[]
        
        
def stop_animation(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()
            
        
         
    

        
        
    
        
    

    
    

pgzrun.go()
    

    
    




