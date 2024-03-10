from subprocess import call
from time import sleep
import patterns

size = 60
grid = [[0 for _ in range(size)] for _ in range(size)]

def check(index_r, index_c):
    index_check_r = index_r - 1
    index_check_c = index_c - 1
    n_neighborns = 0
    for _ in range(3):
        for _ in range(3):
            if index_check_c == index_c and index_check_r == index_r:
                pass
            else:
                try:
                    if grid[index_check_r][index_check_c] == 1:
                        n_neighborns += 1
                except IndexError:
                    pass
            index_check_c += 1
        index_check_c = index_c - 1
        index_check_r += 1

    return n_neighborns

def updateGrid():
    index_c = 0
    index_r = 0
    new_grid = [[0 for _ in range(size)] for _ in range(size)]
    while index_r < len(grid):
        while index_c < len(grid[0]):
            if check(index_r, index_c) == 2:
                if grid[index_r][index_c] == 1:
                    new_grid[index_r][index_c] = 1
                else:
                    new_grid[index_r][index_c] = 0
            elif check(index_r, index_c) == 3:
                new_grid[index_r][index_c] = 1
            else:
                new_grid[index_r][index_c] = 0

            index_c += 1
        index_c = 0
        index_r += 1
    return new_grid

def printGrid(grid):
    call(['clear'])
    for i in grid:
        str_row = ''.join(map(str, i))
        nice_row = str_row.replace('0', '⬜').replace('1', '⬛')
        print(nice_row)
    sleep(0.1)

#patterns.random(grid, 500)
patterns.Glider(grid)
#patterns.Square(grid)
#patterns.OLine(grid)
#patterns.Line(grid)
#patterns.Bar(grid)
#patterns.Cross(grid)

while True:
    printGrid(grid)
    grid = updateGrid()

# ENDFILE
