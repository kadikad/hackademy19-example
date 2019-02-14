class Cell():

    def __init__(self, a_row_i, a_col_i):
        self.current_state = '-' #'-' determines that cell is dead
        self.next_state = 'x'
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

    def make_alive(self):
        self.current_state = 'x'

# overall cell has following information:
# (r_i),(c_i),(neigh),(current_state)
# next step: compute_nest_states():
    #each_n.are_you_alive
        #...

#true alive 
#false not

    def is_alive(self):
        if self.current_state == 'x': # is it the same?
            return True
        else:
            return False

    def compute_next_iteration(self):
        alive_ne = 0 #ne = neighbours
        for ne in self.neigh:
            if ne.is_alive() == True: #if ne in is_alive(self) is equal to True
                alive_ne = alive_ne + 1

        if self.is_alive()==True:
            if (alive_ne == 2 or alive_ne == 3):
                self.next_state = 'x' #I am alive and I remain alive
            else:
                self.next_state = '-' #I die, either of solitude or of noise 
        else:
            if alive_ne == 3:
                self.next_state = 'x' #I resurrect from my ahes
            else:
                self.next_state = '-' #I was dead and I remain dead

        
    def evolve(self):
        self.current_state = self.next_state


