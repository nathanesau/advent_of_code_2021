---
title: Day 04
date: 2021-12-04
modified: 2021-12-04
category: aoc2021
tags: js
Authors: Nathan Esau
---

See problem [here](https://adventofcode.com/2021/day/4).

For part1, we need to do the following:

* define a function which can parse the order and boards from the puzzle input, i.e. `parse_input`
* define a function which marks squares equal to `e` in bingo board as `null`, i.e. `mark_board`
* define a function which can check if a bingo board is solved, i.e. it has a column or row with all `null` entries i.e. `is_solved`
* define a function which can calculate the score for a board which is the sum of non `null` entries, i.e. `calculate_score`
* define a function which calculates the `score` for the `n`th winning board, i.e. `score`

here are these functions

```js
function parse_input(pi) {
    var lines = pi.split('\n').map(String);
    var order = lines[0].split(',').map(Number);
    var boards = [];
    var board = [];
    for (var line of lines.slice(2)) {
        if (line.length === 0) {
            boards.push(board);
            board = [];
            continue;
        }
        var row = line.split(' ').filter(function(value) { return value.trim().length > 0; }).map(Number);
        board.push(row);
    }
    boards.push(board);
    return {order: order, boards: boards};
}

function mark_board(board, e) {
    for(var i = 0; i < board.length; i++) {
        for(var j = 0; j < board[0].length; j++) {
            if (board[i][j] === e) {
                board[i][j] = null;
            }
        }
    }
}

function is_solved(board) {
    for(var i = 0; i < board.length; i++) {
        var rc = 0;
        for(var j = 0; j < board[0].length; j++) {
            if (board[i][j] === null) {
                rc += 1;
            }
        }
        if (rc === board[0].length) {
            return true;
        }
    }
    for (var j = 0; j < board[0].length; j++) {
        var cc = 0;
        for (var i = 0; i < board.length; i++) {
            if (board[i][j] === null) {
                cc += 1;
            }
        }
        if (cc === board.length) {
            return true;
        }
    }
    return false;
}

function calculate_score(board) {
    var s = 0;
    for (var i = 0; i < board.length; i++) {
        for (var j = 0; j < board[0].length; j++) {
            if (board[i][j] !== null) {
                s += board[i][j];
            }
        }
    }
    return s;
}

function score(order, boards, n) {
    var winners = new Set();
    for (var e of order) {
        var index = -1;
        for (var board of boards) {
            index += 1;
            if (winners.has(index)) continue;
            mark_board(board, e);
            if (is_solved(board)) winners.add(index);
            if (winners.size === n) return calculate_score(board) * e;
        }
    }
}
```

then we just want the score for the first winning board.

```js
function part1(pi) {
    var data = parse_input(pi);
    var ans = score(data["order"], data["boards"], 1);
    console.log(`part1: ${ans}`);
}
```

and for part2 we want the score for the second winning board.

```js
function part2(pi) {
    var data = parse_input(pi);
    var ans = score(data["order"], data["boards"], data["boards"].length);
    console.log(`part2: ${ans}`);
}
```

Cracked the top 500 this time. Progress is being made!