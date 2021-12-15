import itertools

def part1(arr):
    count = 0
    for row in arr:
        a, b = row.split('|')
        signals = [e.strip() for e in a.split(' ') if e.strip()]
        outputs = [e.strip() for e in b.split(' ') if e.strip()]
        for output in outputs:
            if len(output) == 2 or len(output) == 4 or \
                len(output) == 3 or len(output) == 7:
                count += 1
    ans = count
    print(ans)

def find_numbers(numbers):
    one = next((x for x in numbers if len(x) == 2))
    four = next((x for x in numbers if len(x) == 4))
    seven = next((x for x in numbers if len(x) == 3))
    eight = next((x for x in numbers if len(x) == 7))
    nine = next((x for x in numbers if len(x) == 6 and all(y in x for y in four)))
    zero = next((x for x in numbers if len(x) == 6 and x != nine and all(y in x for y in one)))
    six = next((x for x in numbers if len(x) == 6 and x != nine and x != zero))
    three = next((x for x in numbers if len(x) == 5 and all(y in x for y in one)))
    five = next((x for x in numbers if len(x) == 5 and x != three and all(y in nine for y in x)))
    two = next((x for x in numbers if len(x) == 5 and x != three and x != five))
    return [zero, one, two, three, four, five, six, seven, eight, nine]

def part2(arr):
    # thanks reddit...
    total = 0
    for row in arr:
        a, b = row.split('|')
        signals = [e.strip() for e in a.split(' ') if e.strip()]
        outputs = [e.strip() for e in b.split(' ') if e.strip()]
        sorted_signals = [sorted(signal) for signal in signals]
        sorted_outputs = [sorted(output) for output in outputs]
        numbers = find_numbers(sorted_signals)
        total += int(''.join([str(numbers.index(x)) for x in sorted_outputs]))
    ans = total
    print(total)

with open('aoc2021_day08.txt') as f:
    data = f.read()

print("day08")
arr = [line for line in data.splitlines()]
part1(arr)
part2(arr)