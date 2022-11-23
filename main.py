from time import sleep
import configurations as configs
from world import World
import pygame
from pygame import Rect
from random import randint
import sys
import numpy as np
pygame.init()

background_color="#C8C6D7"
cell_color = "#006491"
pixel_size = 8
margin = 1
cell_size = (pixel_size + (margin * 2))


def init_world(width, height):
    world = World(width, height)
    print(f"initialised world with dimenions {width} x {height}")

    #set initial conditions
    # configs.random_population(world_map, 500)
    configs.create_blinker(world, 40,40)
    configs.create_toad(world, 100,60)
    return world, width, height

def init_screen():
    info = pygame.display.Info()
    w = info.current_w
    h = info.current_h
    print(f"setting screen size to {w} x {h}")
    screen = pygame.display.set_mode((w, h))
    screen.fill(background_color)
    return screen, w, h


screen, scr_width, scr_height = init_screen()
world, width, height = init_world(int(scr_width/cell_size), int(scr_height/cell_size))
            

def redraw_world():
  for row in world.get_rows():
        for cell in row:
            if cell.is_alive():
                print("Cell alive at", cell.x, cell.y)
                pygame.draw.rect(screen, cell_color, Rect(cell.x*cell_size,cell.y*cell_size,pixel_size,pixel_size))
                # pygame.draw.rect(screen, (255,255,255), Rect(randint(0,width),randint(0,height),pixel_size,pixel_size))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Goodbye, life")
            sys.exit()

    # Draw Matrix
    redraw_world()

    # Update matrix
    world.tick()

    pygame.display.flip()
    sleep(1)
    screen.fill(background_color)