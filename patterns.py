def Square(grid):
    half = int(len(grid) / 2)
    grid[half-1][half-1]     = 1
    grid[half-1][half]   = 1
    grid[half][half-1]   = 1
    grid[half][half] = 1

def Glider(grid):
    grid[1][3] = 1
    grid[2][4] = 1
    grid[3][2] = 1
    grid[3][3] = 1
    grid[3][4] = 1

def Bar(grid):
    half = int(len(grid) / 2)
    grid[half][half-1] = 1
    grid[half][half]   = 1
    grid[half][half+1] = 1

def Line(grid):
    half = int(len(grid) / 2)
    for i,_ in enumerate(range(len(grid))):
        grid[half][i] = 1

def OLine(grid):
    for i in range(len(grid)):
        grid[i][i] = 1

def Cross(grid):
    for i in range(len(grid)):
        grid[i][i+1] = 1
    for r,c in enumerate(range(len(grid),0,-1)):
        grid[r][c-1] = 1

def random(grid, n_of_alive):
    from random import randint
    grid_size = len(grid)
    existAlredy = []
    if n_of_alive > grid_size**2:
        print('More cell alive than cell in the grid!')
        exit()
    else:
        for _ in range(n_of_alive):
            random_c = randint(0, grid_size-1)
            random_r = randint(0, grid_size-1)
            if [random_c, random_r] not in existAlredy:
                grid[random_c][random_r] = 1
            existAlredy.append([random_c, random_r])
