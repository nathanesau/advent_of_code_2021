import sys

def get_neighbors(grid, i, j):
    neighbors = []
    for n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]:
        if n[0] >= 0 and n[0] < len(grid) and n[1] >= 0 and n[1] < len(grid[0]):
            neighbors.append(n)
    return neighbors

def flash_cell(grid, i, j, md):
    if grid[i][j] <= 9: return
    md["nflashes"] += 1
    for n in get_neighbors(grid, i, j): # adjust neighbors
        ni, nj = n
        if grid[ni][nj] <= 9 and grid[ni][nj] != 0:
            grid[ni][nj] += 1
            if grid[ni][nj] > 9:
                flash_cell(grid, ni, nj, md)
    grid[i][j] = 0

def adjust_grid(grid, nsteps, md):
    for step in range(nsteps):
        grid = [[grid[i][j]+1 for j in range(len(grid[0]))] for i in range(len(grid))]
        nflashes_before = md["nflashes"]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                flash_cell(grid, i, j, md)
        nflashes_after = md["nflashes"]
        if (nflashes_after - nflashes_before) == len(grid) * len(grid[0]):
            md["nsteps"] = step+1
            return
    md["nsteps"] = nsteps

def part1(grid):
    md = {"nflashes": 0}
    adjust_grid(grid, nsteps=100, md=md)
    print("part1 ", md["nflashes"])

def part2(grid):
    md = {"nflashes": 0}
    adjust_grid(grid, nsteps=sys.maxsize, md=md)
    print("part2 ", md["nsteps"])

with open("aoc2021_day11.txt") as f:
    data = f.read()

print("day11")
grid = [[int(e) for e in line] for line in data.splitlines()]
part1(grid)
grid = [[int(e) for e in line] for line in data.splitlines()]
part2(grid)
