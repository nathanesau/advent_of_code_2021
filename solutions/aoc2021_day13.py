import ascii_parser  # pip3 install ascii_parser==0.1.4

def parse_input(data):
    coordinates = []
    folds = []
    found_break = False
    for line in data.splitlines():
        if len(line) == 0:
            found_break = True
            continue
        if not found_break: coordinates.append(list(map(int, line.split(','))))
        else: folds.append(line)
    return coordinates, folds

def display_grid(grid): # for debugging purpose
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print()

def fold_grid(grid, f):
    if 'fold along x' in f: # fold along x (vertical) - left
        x = int(f.split('=')[1])
        for i in range(len(grid)):
            for j in range(1, x+1):
                if x - j >= 0 and x + j >= 0 and x - j < len(grid[0]) and x + j < len(grid[0]):
                    if grid[i][x-j] != '#':
                        grid[i][x-j] = grid[i][x+j]
        return [[grid[i][j] for j in range(x)] for i in range(len(grid))]
    else: # fold along y (horizontal) - up
        y = int(f.split('=')[1])
        for i in range(1, y+1):
            for j in range(len(grid[0])):
                if y - i >= 0 and y + i >= 0 and y - i < len(grid) and y + i < len(grid):
                    if grid[y-i][j] != '#':
                        grid[y-i][j] = grid[y+i][j]
        return [[grid[i][j] for j in range(len(grid[0]))] for i in range(y+1)]

def part1(data):
    coordinates, folds = parse_input(data)
    xmax, ymax = max([e[0] for e in coordinates]), max(e[1] for e in coordinates)
    grid = [['.' for _ in range(xmax+1)] for _ in range(ymax+1)]
    for c in coordinates:  # x: col, y: row
        x, y = c
        grid[y][x] = '#'
    for f in folds[:1]:
        grid = fold_grid(grid, f)
    ans = sum([sum([1 if grid[i][j] == '#' else 0 for j in range(len(grid[0]))]) for i in range(len(grid))])
    print("part1 ", ans)

def part2(data):
    coordinates, folds = parse_input(data)
    xmax, ymax = max([e[0] for e in coordinates]), max(e[1] for e in coordinates)
    grid = [['.' for _ in range(xmax+1)] for _ in range(ymax+1)]
    for c in coordinates:  # x: col, y: row
        x, y = c
        grid[y][x] = '#'
    for f in folds:
        grid = fold_grid(grid, f)
    art = '\n'
    art += '\n'.join(['    ' + ''.join(grid[i]) for i in range(len(grid)-1)])
    art += '\n' + '    '
    # the parser is currently terrible and the art has to be in very specific format
    ans = ascii_parser.parser.parse(art)
    print("part2 ", ans)


with open("aoc2021_day13.txt") as f:
    data = f.read()

print("day13")
part1(data)
part2(data)