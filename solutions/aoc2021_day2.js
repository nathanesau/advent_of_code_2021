var fs = require('fs');

function part1(pi) {
    var arr = pi.split('\n').map(String);
    var x = 0;
    var y = 0;
    for(var command of arr) {
        var comp = command.split(" ");
        var direction = comp[0];
        var magnitude = parseInt(comp[1]);
        if (direction === "forward") {
            x += magnitude;
        }
        else if (direction === "down") {
            y += magnitude;
        }
        else if (direction === "up") {
            y -= magnitude;
        }
    }
    var ans = x * y;
    console.log(`part1: ${ans}`);
}

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

console.log("day2");
var f = fs.readFileSync('aoc2021_day2.txt', 'utf8');
var pi = f.toString();
part1(pi);
part2(pi);