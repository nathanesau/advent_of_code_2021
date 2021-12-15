# globals
nflashes = 0

def get_neighbors(grid, i, j):
    neighbors = []
    for n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]:
        if n[0] >= 0 and n[0] < len(grid) and n[1] >= 0 and n[1] < len(grid[0]):
            neighbors.append(n)
    return neighbors

def flash_cell(grid, i, j):
    global nflashes
    if grid[i][j] <= 9:
        return
    nflashes += 1
    for n in get_neighbors(grid, i, j): # adjust neighbors
        ni, nj = n
        if grid[ni][nj] <= 9 and grid[ni][nj] != 0:
            grid[ni][nj] += 1
            if grid[ni][nj] > 9:
                flash_cell(grid, ni, nj)
    grid[i][j] = 0

def display_grid(grid): # for debugging
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print()

def adjust_grid(grid, nsteps):  # return num of steps performed
    global nflashes
    for step in range(nsteps):
        # increment
        grid = [[grid[i][j]+1 for j in range(len(grid[0]))] for i in range(len(grid))]
        # flash
        nflashes_before = nflashes
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                flash_cell(grid, i, j)
        nflashes_after = nflashes
        if (nflashes_after - nflashes_before) == len(grid) * len(grid[0]):
            return step
    return nsteps

def part1(grid):
    global nflashes
    nflashes = 0
    _ = adjust_grid(grid, nsteps=100)
    #display_grid(grid)
    print("part1 ", nflashes)

def part2(grid):
    global nflashes
    nflashes = 0
    performed = adjust_grid(grid, nsteps=1000)
    #display_grid(grid)
    print("part2 ", performed+1)

with open("aoc2021_day11.txt") as f:
    data = f.read()

print("day11")
grid = [[int(e) for e in line] for line in data.splitlines()]
part1(grid)
grid = [[int(e) for e in line] for line in data.splitlines()]
part2(grid)
