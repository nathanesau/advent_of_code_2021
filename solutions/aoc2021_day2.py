def part1(arr):
    x = 0
    y = 0
    for command in arr:
        a, b = command.split(" ")
        direction = a
        magnitude = int(b)
        if direction == "forward":
            x += magnitude
        if direction == "down":
            y += magnitude
        if direction == "up":
            y -= magnitude
    ans = x * y
    print("part1: ", ans)

def part2(arr):
    x = 0
    y = 0
    aim = 0
    for command in arr:
        a, b = command.split(" ")
        direction = a
        magnitude = int(b)
        if direction == "forward":
            x += magnitude
            y += aim * magnitude
        if direction == "down":
            aim += magnitude
        if direction == "up":
            aim -= magnitude
    ans = x * y
    print("part2: ", ans)

with open("aoc2021_day2.txt") as f:
    data = f.read()
    arr = [line for line in data.splitlines()]

print("day2")
part1(arr)
part2(arr)
