---
title: Day 03
date: 2021-12-03
modified: 2021-12-03
category: aoc2021
tags: js
Authors: Nathan Esau
---

See problem [here](https://adventofcode.com/2021/day/3).

For part1, we need to loop through the lines column by column and count the frequency of each digit in the column. If zero is more common, our first string `s1` appends a zero. Otherwise, our first string `s1` appends a one. Our second string is the opposite.

Then we convert both `s1` and `s2` to a number and multiply the result.

```js
function power(pi) {
    var arr = pi.split('\n').map(String);
    var s1 = "";
    var s2 = "";
    for(var j = 0; j < arr[0].length; j++) {
        var c = {'0' : 0, '1': 0};
        for(var i = 0; i < arr.length; i++) {
            var e = arr[i][j];
            c[e] += 1;
        }
        if (c['0'] > c['1']) {
            s1 += "0";
            s2 += "1";
        }
        else {
            s1 += "1";
            s2 += "0";
        }
    }
    var x = parseInt(s1, 2);
    var y = parseInt(s2, 2);
    return x * y;

function part1(pi) {
    var ans = power(pi);
    console.log(`part1: ${ans}`);
}
```

For part2, we loop through the lines column by column and count the frequency of each digit in the *remaining* rows. For oxygen, if zero is more common, our target character is a one. Otherwise, our target character is a zero. For scrubber it is the opposite.

Then we loop through the *remaining rows* and remove the rows which start with the target character. Once we only have one row left, we convert the row to a number.

We multiply the oxygen result by the scrubber result.

```js
function oxygen_scrubber(arr, type) {
    var arr = pi.split('\n').map(String);
    var rows = Array(arr.length).fill().map((_, i) => i);
    for(var j = 0; j < arr[0].length; j++) {
        var c = {'0' : 0, '1': 0};
        for(var i = 0; i < arr.length; i++) {
            if (rows.includes(i)) {
                var e = arr[i][j];
                c[e] += 1;
            }
        }
        var t = (c['0'] > c['1']) ? '1' : '0';
        if (type === "scrubber") {
            t = (t === '1') ? '0' : '1';
        }
        for (var i = 0; i < arr.length; i++) {
            if (!rows.includes(i)) {
                continue;
            }
            if (arr[i][j] === t) {
                var index = rows.indexOf(i);
                rows.splice(index, 1);
            }
            if (rows.length == 1) {
                var i = rows[0];
                var s = arr[i];
                return parseInt(s, 2);
            }
        }
    }
    return null;
}

function part2(pi) {
    var ans = oxygen_scrubber(pi, "oxygen") * oxygen_scrubber(pi, "scrubber");
    console.log(`part2: ${ans}`);
}
```

This one was definitely a little trickier than the first two days.