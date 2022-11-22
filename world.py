from automaton import Automaton

class WorldStats:
    def __init__(self) -> None:
        self.cells=0
        self.underpopulation=0
        self.overpopulation=0
        self.reproduction=0
        self.ticks=0

    def inc_reproduction(self):
        self.reproduction +=1
    
    def inc_underpopulation(self):
        self.underpopulation +=1
    
    def inc_overpopulation(self):
        self.overpopulation +=1
    
    def increment_cells(self):
        self.cells += 1

    def get_cell_count(self):
        return self.cells

    def get_info(self):
        return f"\nTick {self.ticks}: Cells in world: {self.cells} \n Reproduction: {self.reproduction} \n Underpopulation: {self.underpopulation}\n Overpopulation: {self.overpopulation}"

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        self.stats = WorldStats()
        self.operation_buffer = []

        for i in range(width):
            column = []
            for j in range(height):
                column.append(Automaton(self, i, j))
                self.stats.increment_cells()
            self.cells.append(column)
    
    def get_buffer(self):
        return self.operation_buffer

    def get_rows(self):
        return self.cells

    def get_cell(self, x, y):
        return self.cells[x][y]

    def apply_changes(self):
        buf = self.get_buffer()
        print(f"About to apply {len(buf)} changes from buffer")
        while len(buf) > 0:
            m = buf.pop()
            m()
        assert len(buf) == 0

    def tick(self):
        for row in self.cells:
            for c in row:
                c.tick()
        self.stats.ticks +=1
        self.apply_changes()
        print(self.stats.get_info())

    def get_neighbours(self, i, j):
        neighbours = []
        not_left_edge = i > 0
        not_top_edge = j > 0
        not_right_edge = i < self.width-1
        not_bottom_edge = j < self.height-1

        # check each of 8 cells
        if not_left_edge and not_top_edge: neighbours.append(self.cells[i-1][j-1])
        if not_left_edge: neighbours.append(self.cells[i-1][j])
        if not_left_edge and not_bottom_edge: neighbours.append(self.cells[i-1][j+1])

        if not_top_edge: neighbours.append(self.cells[i][j-1])
        if not_bottom_edge: neighbours.append(self.cells[i][j+1])

        if not_right_edge and not_top_edge: neighbours.append(self.cells[i+1][j-1])
        if not_right_edge: neighbours.append(self.cells[i+1][j])
        if not_right_edge and not_bottom_edge: neighbours.append(self.cells[i+1][j+1])
        return neighbours

    def get_stats(self):
        return self.stats