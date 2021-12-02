---
title: Day 2
date: 2021-01-02
modified: 2021-01-02
category: aoc2021
tags: js
Authors: Nathan Esau
---

See problem [here](https://adventofcode.com/2021/day/2).

For part1, we need to keep track of horizontal position `x` and depth `y`.

```js
function part1(pi) {
    var arr = pi.split('\n').map(String);
    var x = 0;
    var y = 0;
    for(var command of arr) {
        var comp = command.split(" ");
        var direction = comp[0];
        var magnitude = parseInt(comp[1]);
        if (direction === "forward") x += magnitude;
        else if (direction === "down") y += magnitude;
        else if (direction === "up") y -= magnitude;
    }
    var ans = x * y;
    console.log(`part1: ${ans}`);
}
```

For part2, we need to keep track of horizontal position `x` and depth `y` and aim. Note that the up and down directions now change the aim not the depth.

```js
function part2(pi) {
    var arr = pi.split('\n').map(String);
    var x = 0;
    var y = 0;
    var aim = 0;
    for (var command of arr) {
        var comp = command.split(" ");
        var direction = comp[0];
        var magnitude = parseInt(comp[1]);
        if (direction === "forward") {
            x += magnitude;
            y += aim * magnitude;
        }
        else if (direction === "down") {
            aim += magnitude;
        }
        else if (direction === "up") {
            aim -= magnitude;
        }
    }
    var ans = x * y;
    console.log(`part2: ${ans}`);
}
```

That's all for today. Nothing too tricky yet!