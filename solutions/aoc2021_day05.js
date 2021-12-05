var fs = require('fs');

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

function num_overlapping(grid) {
    var t = 0;
    for (var i = 0; i < grid.length; i++) {
        for (var j = 0; j < grid[0].length; j++) {
            if (grid[i][j] > 1) t += 1;
        }
    }
    return t;
}

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

function part1(pi) {
    var ans = calculate_overlapping(pi, false);
    console.log(`part1: ${ans}`);
}

function part2(pi) {
    var ans = calculate_overlapping(pi, true);
    console.log(`part2: ${ans}`);
}

console.log("day05");
var f = fs.readFileSync('aoc2021_day05.txt', 'utf8');
var pi = f.toString();
part1(pi);
part2(pi);