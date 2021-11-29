var fs = require('fs');

function part1(pi) {
    var arr = pi.split(', ');
    var x = 0;
    var y = 0;
    var angle = 0;
    for (const instruction of arr) {
        var direction = instruction.charAt(0);
        var magnitude = parseInt(instruction.substring(1));
        angle = (direction == 'L') ? angle - 90 : angle + 90;
        angle = (angle < 0) ? angle + 360 : (angle >= 360) ? angle - 360 : angle;
        x = (angle == 90) ? x + magnitude : (angle == 270) ? x - magnitude : x;
        y = (angle == 0) ? y + magnitude : (angle == 180) ? y - magnitude : y;
    }
    ans = Math.abs(x) + Math.abs(y);
    console.log(`part 1: ${ans}`);
}

function part2(pi) {
    // need to use JSON.stringify for deep equality
    // see https://stackoverflow.com/a/49782781/2557235
    var arr = pi.split(', ');
    var x = 0;
    var y = 0;
    var angle = 0;
    var visited = new Set();
    for (const instruction of arr) {
        var direction = instruction.charAt(0);
        var magnitude = parseInt(instruction.substring(1));
        angle = (direction == 'L') ? angle - 90 : angle + 90;
        angle = (angle < 0) ? angle + 360 : (angle >= 360) ? angle - 360 : angle;
        var found = false;
        for (var i = 0; i < magnitude; i++) {
            x = (angle == 90) ? x + 1 : (angle == 270) ? x - 1 : x;
            y = (angle == 0) ? y + 1 : (angle == 180) ? y - 1 : y;
            var entry = { x: x, y: y };
            if (visited.has(JSON.stringify(entry))) {
                found = true;
                break;
            }
            visited.add(JSON.stringify(entry));
        }
        if (found) {
            break;
        }
    }
    var ans = Math.abs(x) + Math.abs(y);
    console.log(`part 2: ${ans}`);
}

var f = fs.readFileSync('aoc2016_day1.txt', 'utf8');
var pi = f.toString();
part1(pi);
part2(pi);
