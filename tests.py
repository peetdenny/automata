import unittest
from world import World


class TestAutomata(unittest.TestCase):
    def testWorld(self):
        world = World(50,50)
        cell = world.get_cell(4,4)
        print(cell)
        self.assertEquals(cell.x, 4)
        self.assertEquals(cell.y, 4)

        neighbours = world.get_neighbours(4,4)
        self.assertEquals(8, len(neighbours), "This cell should have 8 neighbours")

        neighbours = world.get_neighbours(0,4)
        self.assertEquals(5, len(neighbours), "top row should have 5 neighbours")

        neighbours = world.get_neighbours(4,49)
        self.assertEquals(5, len(neighbours), "bottom row should have 5 neighbours")
        
        neighbours = world.get_neighbours(0,0)
        self.assertEquals(3, len(neighbours), "top left corner should have 3 neighbours")
        self.assertEquals(0, neighbours[0].x, "The first neighbour should have position x=0")
        

if __name__ == '__main__':
    unittest.main()
