---
title: Day 01
date: 2021-01-01
modified: 2021-01-01
category: aoc2021
tags: js
Authors: Nathan Esau
---

See problem [here](https://adventofcode.com/2021/day/1).

For part1, we need to determine the number of entries larger than the previous entry.

```js
function part1(pi) {
    var arr = pi.split('\n').map(Number);
    var ans = 0;
    var pe = null;
    for (var e of arr) {
        if (pe != null && e > pe) ans += 1;
        pe = e;
    }
    console.log(`part1: ${ans}`);
}
```

For part2, we check the number of 3-entry moving average larger than the previous moving average.

```js
function part2(pi) {
    var arr = pi.split('\n').map(Number);
    var ans = 0;
    var a = null;
    var b = null;
    var ps = null;
    for(e of arr) {
        if (a != null && b != null) {
            var s = a + b + e;
            if (ps != null && s > ps) ans += 1;
            ps = s;
        }
        b = a;
        a = e;
    }
    console.log(`part 2: ${ans}`);
}
```

Not much else to say here!
