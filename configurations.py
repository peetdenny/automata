from random import randint

def getWidth(world):
    return world.shape[0]

def getHeight(world):
    return world.shape[1]

def random_population(world, size):
    for i in range(size):
        world[randint(0,getWidth()-1), randint(0,getHeight()-1)] = 1


# Still lifes

def create_beehive(world, x, y):
    world.get_cell(x-1,y-1).alive=1
    world.get_cell(x,y-1).alive=1

    world.get_cell(x-2,y).alive=1
    world.get_cell(x+1,y).alive=1

    world.get_cell(x-1,y+1).alive=1
    world.get_cell(x,y+1).alive=1


# Oscillators

def create_blinker(world, x, y):
    world.get_cell(x,y).alive = 1
    world.get_cell(x-1,y).alive = 1
    world.get_cell(x+1,y).alive = 1


def create_toad(world, x, y):
    world.get_cell(x-2,y).alive=1
    world.get_cell(x-2,y+1).alive=1
    world.get_cell(x-1,y+2).alive=1
    
    world.get_cell(x,y-1).alive=1
    world.get_cell(x+1,y).alive=1
    world.get_cell(x+1,y+1).alive=1


# Spaceships

def create_glider(world, x, y):
    world.get_cell(x-1,y-1).alive = 1
    
    world.get_cell(x,y).alive = 1
    world.get_cell(x+1,y).alive = 1
    
    world.get_cell(x-1,y+1).alive = 1
    world.get_cell(x,y+1).alive = 1

# Methuselahs
def create_the_R_pentomino(world, x, y):
    """ Creates The R-Pentomino"""
    world.get_cell(x,y).alive = 1
    world.get_cell(x,y-1).alive = 1
    world.get_cell(x,y+1).alive = 1
    world.get_cell(x-1,y).alive = 1
    world.get_cell(x+1,y-1).alive = 1


def create_the_B_pentomino(world, x, y):
    """ Creates The B-Pentomino"""
    world.get_cell(x-1,y-1).alive = 1
    world.get_cell(x+1,y-1).alive = 1
    world.get_cell(x+2,y-1).alive = 1

    world.get_cell(x-1,y).alive = 1
    world.get_cell(x,y).alive = 1
    world.get_cell(x+1,y).alive = 1

    world.get_cell(x,y+1).alive = 1

def create_the_Pi_pentomino(world, x, y):
    """ Creates The π-Pentomino"""
    world.get_cell(x-1,y-1).alive = 1
    world.get_cell(x,y-1).alive = 1
    world.get_cell(x+1,y-1).alive = 1

    world.get_cell(x-1,y).alive = 1
    world.get_cell(x+1,y).alive = 1

    world.get_cell(x-1,y+1).alive = 1
    world.get_cell(x+1,y+1).alive = 1

def create_Thunderbird(world, x, y):
    """ Creates The Thunderbird Methuselah"""
    world.get_cell(x-1,y-1).alive = 1
    world.get_cell(x,y-1).alive = 1
    world.get_cell(x+1,y-1).alive = 1

    world.get_cell(x,y+1).alive = 1
    world.get_cell(x,y+2).alive = 1
    world.get_cell(x,y+3).alive = 1
    
# Set pieces

def classic_config1(world):
    """ 4 gliders spawn beautiful large symmetries. ~1500 generations"""
    create_blinker(world, 40,40)
    create_toad(world, 100,60)
    create_glider(world, 14, 14)
    create_glider(world, 3, 3)
    create_glider(world, 52, 14)
    create_glider(world, 42, 3)


def annihilation1(world):
    """ Two beehives and a glider totally annihilate"""
    create_beehive(world, 50, 15)
    create_beehive(world, 50, 20)
    create_glider(world,34, 5)
