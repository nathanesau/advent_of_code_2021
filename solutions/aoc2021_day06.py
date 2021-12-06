import copy

def part1(arr):
    fishes = [int(e) for e in arr[0].split(',')]
    pop = copy.deepcopy(fishes)
    for _ in range(80):
        n = len(pop)
        for i in range(n):
            if pop[i] > 0:
                pop[i] -= 1
            else:
                pop[i] = 6
                pop.append(8)
    ans = len(pop)
    print(ans)

def part2(arr):
    fishes = [int(e) for e in arr[0].split(',')]
    count = dict((fish, 0) for fish in fishes)
    for fish in fishes: count[fish] += 1
    for _ in range(256):
        new_count = {}
        for k, v in count.items():
            if k > 0:
                if k-1 not in new_count: new_count[k-1] = 0
                new_count[k-1] += v
            else:
                if 6 not in new_count: new_count[6] = 0
                if 8 not in new_count: new_count[8] = 0
                new_count[6] += v
                new_count[8] += v
        count = new_count
    ans = sum(count.values())
    print(ans)

with open("aoc2021_day06.txt") as f:
    data = f.read()
    arr = [line for line in data.splitlines()]

print("day06")
part1(arr)
part2(arr)
