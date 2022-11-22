

class Automaton:
    
    def __init__(self, world, x, y):
        self.x = x
        self.y = y
        self.alive=0
        self.world = world
        self.stats = world.stats

    def is_alive(self):
        return self.alive
    
    def revive(self):
        self.alive = 1

    def kill(self):
        self.alive=0
    
    def tick(self):
        neighbours = self.world.get_neighbours(self.x, self.y)
        live_neighbours = 0
        for n in neighbours:
            if n.is_alive():
                live_neighbours +=1
        if live_neighbours > 0: print(f"Cell at position {self.x},{self.y} has {live_neighbours} live neighbours and {len(neighbours)} neighbours total")
        # we need this to queue up operations so as not to have phantom automata - those that were alive, but were killed during the current tick
        buf = self.world.get_buffer() 

        if self.alive == 0 and live_neighbours == 3:
            buf.append(self.revive) #self.alive = 1
            self.stats.inc_reproduction()
            return
        # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        if self.alive == 1 and live_neighbours < 2: 
            buf.append(self.kill) #self.alive = 0
            self.stats.inc_underpopulation()
            return
        # Any live cell with two or three live neighbours lives on to the next generation.
        # Any live cell with more than three live neighbours dies, as if by overpopulation
        if self.alive == 1 and live_neighbours > 3:
           buf.append(self.kill) # self.alive = 0
           self.stats.inc_overpopulation()
    
    
