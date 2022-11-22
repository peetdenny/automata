from random import randint

def getWidth(world):
    return world.shape[0]

def getHeight(world):
    return world.shape[1]

def random_population(world, size):
    for i in range(size):
        world[randint(0,getWidth()-1), randint(0,getHeight()-1)] = 1

def create_blinker(world, x, y):
    world[x,y]=1
    world[x-1,y]=1
    world[x+1,y]=1
