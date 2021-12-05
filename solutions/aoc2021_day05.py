def parse_input(arr):
    segments = []
    for line in arr:
        a, b = line.split('->')
        a1, a2 = a.split(',')
        b1, b2 = b.split(',')
        segment = {"x1": int(a1), "y1": int(a2),
            "x2": int(b1), "y2": int(b2)}
        segments.append(segment)
    return segments

def max_segments(segments):
    maxx = -float('Inf')
    maxy = -float('Inf')
    for segment in segments:
        maxx = max(max(segment["x1"], segment["x2"]), maxx)
        maxy = max(max(segment["y1"], segment["y2"]), maxy)
    return maxx, maxy

def display_grid(grid): # for debugging
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 0):
                print('.', end="")
            else:
                print(grid[i][j], end="")
        print("")

def num_overlapping(grid):
    t = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] > 1):
                t += 1
    return t

def calculate_overlapping(arr, include_diagonal):
    segments = parse_input(arr)
    maxx, maxy = max_segments(segments)
    grid = [[0 for _ in range(0, maxx + 1)] for _ in range(0, maxy + 1)]
    for segment in segments:
        x1, x2, y1, y2 = segment["x1"],  segment["x2"], segment["y1"], segment["y2"]
        xincr = 1 if x2 >= x1 else -1
        yincr = 1 if y2 >= y1 else -1
        if (x1 == x2 or y1 == y2): # vertical or horizontal
            for x in range(x1, x2 + 1 if x2 >= x1 else x2 - 1, xincr):
                for y in range(y1, y2 + 1 if y2 >= y1 else y2 - 1, yincr):
                    grid[x][y] += 1
        elif include_diagonal and abs(x1 - x2) == abs(y1 - y2): # diagonal (45)
            x, y = x1, y1
            grid[x][y] += 1
            while x != x2 and y != y2:
                x, y = x + xincr, y + yincr
                grid[x][y] += 1
    return num_overlapping(grid)

def part1(arr):
    ans = calculate_overlapping(arr, False)
    print(ans)

def part2(arr):
    ans = calculate_overlapping(arr, True)
    print(ans)

with open("aoc2021_day05.txt") as f:
    data = f.read()
    arr = [line for line in data.splitlines()]

print("day05")
part1(arr)
part2(arr)
