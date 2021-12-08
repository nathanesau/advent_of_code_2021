import copy
import statistics

def fuel_cost(positions, m, method="constant"):
    cost = 0
    for c in positions:
        if method == "constant":
            cost += abs(m - c)
        else: # "step"
            cost += abs(m - c) * (abs(m - c) + 1) // 2
    return cost

def min_fuel_cost(positions, method="constant"):
    m = int(statistics.median(positions))
    cost = {m: fuel_cost(positions, m, method),
        m-1: fuel_cost(positions, m-1, method),
        m+1: fuel_cost(positions, m+1, method)}
    n = m-1 if cost[m-1] < cost[m] else m+1 if cost[m+1] < cost[m] else m
    if n == m: return cost[m]
    incr = -1 if n == m-1 else +1
    prev = m
    while cost[n] < cost[prev]:
        prev = n
        n += incr
        cost[n] = fuel_cost(positions, n, method)
    return cost[prev]

def part1(arr):
    positions = [int(e) for e in arr[0].split(',')]
    ans = min_fuel_cost(positions)
    print(ans)

def part2(arr):
    positions = [int(e) for e in arr[0].split(',')]
    ans = min_fuel_cost(positions, method="step")
    print(ans)

with open("aoc2021_day07.txt") as f:
    data = f.read()
    arr = [line for line in data.splitlines()]

print("day07")
part1(arr)
part2(arr)
