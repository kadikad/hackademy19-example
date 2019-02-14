from cell import *
import random

def setup_game(size,max_alive):
    a_grid = get_empty_grid(size)
    fill_grid_random(a_grid,max_alive)


def get_empty_grid(size):
    new_grid = []
    for r_i in range(size):
        new_sublist = []
        for c_i in range(size):
            # new_sublist.append('-')
            a_new_cell = Cell(r_i,c_i)
            new_sublist.append(a_new_cell)
        new_grid.append(new_sublist)
    return new_grid


def rand_alive():
    number = random.randint(1,2)
    if number == 1:
        return True
    else:
        return False



def fill_grid_random(a_grid,max_alive):
    size = len(a_grid)
    remaining = max_alive
    for r_i in range(size):
        for c_i in range(size):
            if (remaining > 0) and (rand_alive() == True):
                a_grid[r_i][c_i] = 'X'
                remaining = remaining - 1
            else:
                a_grid[r_i][c_i] = '-'

# [['-','-','-'],
# ['-','X','-'],
# ['-','-','-']]
# prints the following on screen:
# ---
# -X-
# ---
def print_grid(a_grid):
    size = len(a_grid)
    for r_i in range(size):
        for c_i in range(size):
            a_cell = a_grid[r_i][c_i]
            a_cell.print_myself()
        print("")