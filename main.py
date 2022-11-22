from time import sleep
import configurations as configs
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
    width = int(width / cell_size)
    height = int(height / cell_size)
    world_map = np.zeros((width, height))
    print(f"initialised world with dimenions {width} x {height}")

    #set initial conditions
    # configs.random_population(world_map, 500)
    configs.create_blinker(world_map, 40,40)


    return world_map, width, height

def init_screen():
    info = pygame.display.Info()
    w = info.current_w
    h = info.current_h
    print(f"setting screen size to {w} x {h}")
    screen = pygame.display.set_mode((w, h))
    screen.fill(background_color)
    return screen, w, h


screen, scr_width, scr_height = init_screen()
world, width, height = init_world(scr_width, scr_height)

def count_live_neighbours(i,j):
    count = 0
    not_left_edge = i > 0
    not_top_edge = j > 0
    not_right_edge = i < width-1
    not_bottom_edge = j < height-1

    # check each of 9 cells
    if not_left_edge and not_top_edge and world[i-1,j-1] == 1: count +=1
    if not_left_edge and world[i-1,j] == 1: count +=1 
    if not_left_edge and not_bottom_edge and world[i-1,j+1] == 1: count +=1 

    if not_top_edge and world[i,j-1] == 1: count +=1 
    if not_bottom_edge and world[i,j+1] == 1: count +=1 

    if not_right_edge and not_top_edge and world[i+1,j-1] == 1: count +=1 
    if not_right_edge and world[i+1,j] == 1: count +=1 
    if not_right_edge and not_bottom_edge and world[i+1,j+1] == 1: count +=1 
    return count

def update_world():
    for i in range(width):
        for j in range(height):
            live_neighbours = count_live_neighbours(i,j)
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if world[i,j] == 0 and live_neighbours == 3:
                world[i,j] = 1
            # if live_neighbours > 0: print(f"Cell at position {i},{j} has {live_neighbours} live neighbours")
            # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            if world[i,j] == 1 and live_neighbours < 2: 
                world[i,j] = 0
            # Any live cell with two or three live neighbours lives on to the next generation.
            # Any live cell with more than three live neighbours dies, as if by overpopulation
            if world[i,j] == 1 and live_neighbours > 3:
                world[i,j] = 0
            

def redraw_world():
  for i in range(width):
        for j in range(height):
            if world[i,j] ==1:
                pygame.draw.rect(screen, cell_color, Rect(i*cell_size,j*cell_size,pixel_size,pixel_size))
                # pygame.draw.rect(screen, (255,255,255), Rect(randint(0,width),randint(0,height),pixel_size,pixel_size))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Goodbye, life")
            sys.exit()

    # Draw Matrix
    redraw_world()

    # Update matrix
    update_world()

    pygame.display.flip()
    sleep(1)
    screen.fill(background_color)