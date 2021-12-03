def power(arr):
    s1 = ""
    s2 = ""
    for j in range(len(arr[0])):
        c = {'0': 0, '1': 0}
        for i in range(len(arr)):
            c[arr[i][j]] += 1
        if c['0'] > c['1']:
            s1 += "0"
            s2 += "1"
        else:
            s1 += "1"
            s2 += "0"
    x = int(s1, 2)
    y = int(s2, 2)
    ans = x * y
    return ans

def oxygen_scrubber(arr, type):
    rows = set([i for i in range(len(arr))])
    for j in range(len(arr[0])):
        c = {'0': 0, '1': 0}
        for i in range(len(arr)):
            if i in rows:
                c[arr[i][j]] += 1
        if type == "oxygen":
            t = '1' if c['0'] > c['1'] else '0'
        else: # scrubber
            t = '0' if c['0'] > c['1'] else '1'
        for i in range(len(arr)):
            if i not in rows:
                continue
            if arr[i][j] == t:
                rows.remove(i)
            if len(rows) == 1:
                scrubber = int(arr[list(rows)[0]], 2)
                return scrubber
    return None

def part1(arr):
    ans = power(arr)
    print(ans)

def part2(arr):
    x = oxygen_scrubber(arr, "oxygen")
    y = oxygen_scrubber(arr, "scrubber")
    ans = x * y
    print(ans)

with open("aoc2021_day03.txt") as f:
    data = f.read()
    arr = [line for line in data.splitlines()]

print("day03")
part1(arr)
part2(arr)
