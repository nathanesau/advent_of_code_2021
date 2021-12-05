---
title: Day 05
date: 2021-12-05
modified: 2021-12-05
category: aoc2021
tags: js
Authors: Nathan Esau
---

See problem [here](https://adventofcode.com/2021/day/5).

First let's consider how to parse the input:

```js
function parse_input(pi) {
    var arr = pi.split('\n').map(String);
    var segments = [];
    for (var line of arr) {
        var ab = line.split('->');
        var a = ab[0].split(',');
        var b = ab[1].split(',');
        segments.push({
            "x1": parseInt(a[0]), "y1": parseInt(a[1]),
            "x2": parseInt(b[0]), "y2": parseInt(b[1])
        });
    }
    return segments;
}
```

OK. Now that we have that out of the way let's define a function which can calculate the `num_overlapping` lines for a grid.

```js
// for reference, initialize n*n grid like this in js
// Array.from({length:n}, (_,i) => Array.from({length:n}, (_,j) => 0))
function num_overlapping(grid) {
    var t = 0;
    for (var i = 0; i < grid.length; i++) {
        for (var j = 0; j < grid[0].length; j++) {
            if (grid[i][j] > 1) t += 1;
        }
    }
    return t;
}
```

Let's assume that the max size of the grid will be 1000 (reasonable based on puzzle input). We have following line cases to consider:

* If `x1 == x2` we have a horizontal line (I am treating `x` as the row index and `y` as the column index. Transpose of this will work as well...)
* If `y1 == y2` we have a vertical line
* If `Math.abs(segment.x1 - segment.x2) == Math.abs(segment.y1 - segment.y2)` we have a diagonal line (45 degrees)

Note that diagonal line is only included for part2.

We always will go through the point `(x1, y1)`. Then we will move from `(x1, y1)` to `(x2, y2)` and mark all those points as well (including the end point). We can use following logic to increment/ decrement `x` and `y`.

```js
if (segment.x2 !== segment.x1) x = (segment.x2 >= segment.x1) ? x + 1: x - 1;
if (segment.y2 !== segment.y1) y = (segment.y2 >= segment.y1) ? y + 1: y - 1;
```

Then it's just a matter of putting it all together:

```js
function calculate_overlapping(pi, include_diagonal) {
    var segments = parse_input(pi);
    var grid = Array.from({length:1000}, (_,i) => Array.from({length:1000}, (_,j) => 0))
    for (var segment of segments) {
        if (segment.x1 === segment.x2 || segment.y1 === segment.y2 ||
            (include_diagonal && Math.abs(segment.x1 - segment.x2) === Math.abs(segment.y1 - segment.y2))) {
            var x = segment.x1;
            var y = segment.y1;
            grid[x][y] += 1;
            while (x !== segment.x2 || y !== segment.y2) {
                if (segment.x2 !== segment.x1) x = (segment.x2 >= segment.x1) ? x + 1: x - 1;
                if (segment.y2 !== segment.y1) y = (segment.y2 >= segment.y1) ? y + 1: y - 1;
                grid[x][y] += 1;
            }
        }
    }
    return num_overlapping(grid);
}
```

Here are my functions for `part1` and `part2` for reference.

```js
function part1(pi) {
    var ans = calculate_overlapping(pi, false);
    console.log(`part1: ${ans}`);
}

function part2(pi) {
    var ans = calculate_overlapping(pi, true);
    console.log(`part2: ${ans}`);
}
```

Didn't do quite as well on leaderboard this time. Took me about 20 minutes to come up with this approach and a little longer to clean up the code.

Cool problem!