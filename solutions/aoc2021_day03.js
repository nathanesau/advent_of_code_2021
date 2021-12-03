var fs = require('fs');

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
}

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

function part1(pi) {
    var ans = power(pi);
    console.log(`part1: ${ans}`);
}

function part2(pi) {
    var ans = oxygen_scrubber(pi, "oxygen") * oxygen_scrubber(pi, "scrubber");
    console.log(`part2: ${ans}`);
}

console.log("day03");
var f = fs.readFileSync('aoc2021_day03.txt', 'utf8');
var pi = f.toString();
part1(pi);
part2(pi);