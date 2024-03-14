from subprocess import call
from time import sleep
import patterns
from sys import argv

start = False
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
    global start
    call(['clear'])
    for i in grid:
        str_row = ''.join(map(str, i))
        nice_row = str_row.replace('0', '⬜').replace('1', '⬛')
        print(nice_row)
    if start == False:
        input('Press enter to start')
        start = True
    sleep(0.1)

def pattern_arg(arg):
    if arg == 'random'     : patterns.random(grid, 500)
    elif arg == 'glider'   : patterns.Glider(grid)
    elif arg == 'glidergun': patterns.GliderGun(grid)
    elif arg == 'square'   : patterns.Square(grid)
    elif arg == 'oline'    : patterns.OLine(grid)
    elif arg == 'line'     : patterns.Line(grid)
    elif arg == 'bar'      : patterns.Bar(grid)
    elif arg == 'cross'    : patterns.Cross(grid)
    elif arg == 'create'   : patterns.create(grid)
    else:
        print('Invalid pattern')
        exit()

try:
    pattern_arg(argv[1].lower())
except IndexError:
    print('Input a pattern\nExample: python3 main.py GliderGun')
    exit()

while True:
    printGrid(grid)
    grid = updateGrid()

# ENDFILE
