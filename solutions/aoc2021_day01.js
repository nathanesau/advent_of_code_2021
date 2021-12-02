var fs = require('fs');

function part1(pi) {
    var arr = pi.split('\n').map(Number);
    var ans = 0;
    var pe = null;
    for(var e of arr) {
        if (pe != null) {
            if (e > pe) {
                ans += 1;
            }
        }
        pe = e;
    }
    console.log(`part1: ${ans}`);
}

function part2(pi) {
    var arr = pi.split('\n').map(Number);
    var ans = 0;
    var a = null;
    var b = null;
    var ps = null;
    for(e of arr) {
        if (a != null && b != null) {
            var s = a + b + e;
            if (ps != null) {
                if (s > ps) {
                    ans += 1;
                }
            }
            ps = s;
        }
        b = a;
        a = e;
    }
    console.log(`part2: ${ans}`);
}

console.log("day01")
var f = fs.readFileSync('aoc2021_day01.txt', 'utf8');
var pi = f.toString();
part1(pi);
part2(pi);