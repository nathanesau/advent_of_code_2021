var fs = require('fs');

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

function part1(pi) {
    var ans = count_fish(pi, 80);
    console.log(`part1: ${ans}`);
}

function part2(pi) {
    var ans = count_fish(pi, 256);
    console.log(`part2: ${ans}`);
}

console.log("day06");
var f = fs.readFileSync('aoc2021_day06.txt', 'utf8');
var pi = f.toString();
part1(pi);
part2(pi);