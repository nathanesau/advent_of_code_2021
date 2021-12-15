# start: Dec 14, 1:16PM PST
# end part1: Dec 14, 1:28PM PST
# end part2: Dec 14, 1:35PM PST
def first_invalid(line):
    match = {'{': '}', '(': ')', '[': ']', '<': '>'}
    s = []
    for c in line:
        if c in ['[', '(', '{', '<']:
            s.insert(0, c)
        else:
            if not s: raise Exception("can't determine invalid cause")
            o = s.pop(0)
            if match[o] != c: return c, s
    if s: return None, s # allow incomplete lines
    return None, s

def part1(arr):
    pts = {')': 3, ']': 57, '}': 1197, '>': 25137}
    tot = 0
    for line in arr:
        c, s = first_invalid(line)
        if c: tot += pts[c]
    ans = tot
    print("part1 ", ans)

def part2(arr):
    pts = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in arr:
        c, s = first_invalid(line)
        if not c: # incomplete
            match = {'{': '}', '(': ')', '[': ']', '<': '>'}
            score = 0
            while s:
                o = s.pop(0)
                c = match[o]
                score = score * 5 + pts[c]
            scores.append(score)
    ans = sorted(scores)[len(scores)//2]
    print("part2 ", ans)

with open("aoc2021_day10.txt") as f:
    data = f.read()

print("day10")
arr = [line for line in data.splitlines()]
part1(arr)
part2(arr)
