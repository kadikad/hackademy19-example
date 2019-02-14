class Cell():

    def __init__(self, a_row_i, a_col_i):
        self.current_state = '-'
        self.r_i = a_row_i
        self.c_i = a_col_i
    
    def print_myself(self):
        print(self.current_state,end="")
    
    def find_neigh(self,a_grid):
        max_size_0 = len(a_grid) - 1
        neighbours = []
        r = self.r_i
        c = self.c_i
        if r > 0:
            neighbours.append(a_grid[r-1][c])
            if c > 0:
                neighbours.append(a_grid[r-1][c-1])
            if c < max_size_0:
                neighbours.append(a_grid[r-1][c+1])
        # same row
        if c > 0:
            neighbours.append(a_grid[r][c-1])
        if c < max_size_0:
            neighbours.append(a_grid[r][c+1])
        # lower row
        if r < max_size_0:
            neighbours.append(a_grid[r+1][c])
            if c > 0:
                neighbours.append(a_grid[r+1][c-1])
            if c < max_size_0:
                neighbours.append(a_grid[r+1][c+1])
        self.neigh = neighbours

