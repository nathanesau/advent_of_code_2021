---
title: Day 06
date: 2021-12-06
modified: 2021-12-06
category: aoc2021
tags: js, python
Authors: Nathan Esau
---

See problem [here](https://adventofcode.com/2021/day/6).

My initial approach was to track all of the fish. We decrease number of days for each fish by 1 until it reaches 0. Then we reset it to 6 for existing fish and add a new fish with value 8. This works fine but it is too slow for part 2.

```python
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
```

Then I realized that all fish with value `x` are the same so we can just keep track of the count of each fish.

The idea would be if there are `v` fish with value `k`, then the next day there will by `v` more fish with value `k-1` if `k > 0`. Similarly, if `k == 0`, then there will be `v` more fish the next with value 6 and `v` more fish the next value with value 8. This solution is much faster.

```js
function count_fish(pi, days) {
    var initial = pi.split(',').map(Number);
    var count = {};
    for (var fish of initial) {
        if (count[fish] === undefined) count[fish] = 0;
        count[fish] += 1;
    }
    for (var day = 0; day < days; day++) {
        var new_count = {};
        for (const k in count) {
            const v = count[k];
            if (k > 0) {
                if (new_count[k-1] === undefined) new_count[k-1] = 0;
                new_count[k-1] += v;
            }
            else {
                if (new_count[6] === undefined) new_count[6] = 0;
                if (new_count[8] === undefined) new_count[8] = 0;
                new_count[6] += v;
                new_count[8] += v;
            }
        }
        count = new_count;
    }
    return Object.values(count).reduce(function(a, b) { return a + b; });
}
```

For part1, we want the result after 80 days and for part2, we want the result after 256 days.

```js
function part1(pi) {
    var ans = count_fish(pi, 80);
    console.log(`part1: ${ans}`);
}

function part2(pi) {
    var ans = count_fish(pi, 256);
    console.log(`part2: ${ans}`);
}
```

This one was easier than day 5, at least for me.