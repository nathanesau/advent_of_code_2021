---
title: Day 07
date: 2021-12-07
modified: 2021-12-07
category: aoc2021
tags: js, python
Authors: Nathan Esau
---

See problem [here](https://adventofcode.com/2021/day/7).

The basic idea is to calculate the total `cost` for some positions to position `m`.

```js
function fuel_cost(positions, m, method) {
    var cost = 0;
    for (var c of positions) {
        if (method === "constant") {
            cost += Math.abs(m - c);
        }
        else { // "step"
            cost += Math.abs(m - c) * (Math.abs(m - c) + 1) / 2;
        }
    }
    return cost;
}
```

Note that for `part2` the cost function is different. It is (1 + 2 + ... + n) = (n)(n+1)/2.

Probably you can try add possible positions from `min(positions)` to `max(positions)`. But this is kind of stupid. You can instead try median and than branch out from the median in the proper direction (i.e. up or down) until you arrive at the solution. For the provided example, in part 2, I would start at 2 and go up until 5. This is because `fuel_cost(positions, 6, "constant")` is higher than `fuel_cost(positions, 5, "constant")` so I stop.

```js
function min_fuel_cost(positions, method) {
    var m = median(positions);
    var cost = {};
    cost[m] = fuel_cost(positions, m, method);
    cost[m-1] = fuel_cost(positions, m-1, method);
    cost[m+1] = fuel_cost(positions, m+1, method);
    var n = (cost[m-1] < cost[m]) ? m-1 : (cost[m+1] < cost[m]) ? m+1 : m;
    if (n === m) return cost[m];
    var incr = (n === m-1) ? -1 : +1;
    var prev = m;
    while (cost[n] < cost[prev]) {
        prev = n;
        n += incr;
        cost[n] = fuel_cost(positions, n, method);
    }
    return cost[prev];
}
```

And here is the code for `part1` and `part2` using these functions.

```js
function part1(pi) {
    var positions = pi.split(',').map(Number);
    var ans = min_fuel_cost(positions, "constant");
    console.log(`part1: ${ans}`);
}

function part2(pi) {
    var positions = pi.split(',').map(Number);
    var ans = min_fuel_cost(positions, "step");
    console.log(`part2: ${ans}`);
}
```

If you enjoyed this post, please like the post! Looking forward to day 8!