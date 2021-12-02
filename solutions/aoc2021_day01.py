def part1(arr):
    ans = 0
    pe = None
    for e in arr:
        if pe is not None:
            if e > pe:
                ans += 1
        pe = e
    print("part1: ", ans)

def part2(arr):
    ans = 0
    a = None
    b = None
    ps = None
    for e in arr:
        if a is not None and b is not None:
            s = a + b + e
            if ps is not None:
                if s > ps:
                    ans += 1
            ps = s
        b = a
        a = e
    print("part2: ", ans)

with open("aoc2021_day01.txt") as f:
    data = f.read()
    arr = [int(line) for line in data.splitlines()]

print("day01")
part1(arr)
part2(arr)
