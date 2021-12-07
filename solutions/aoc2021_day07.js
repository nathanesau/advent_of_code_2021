var fs = require('fs');

const median = (arr) => {
    const mid = Math.floor(arr.length / 2);
    var nums = [...arr].sort((a, b) => a - b);
    return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};

function fuel_cost(positions, m, method) {
    var cost = 0;
    for (var c of positions) {
        if (method === "constant") {
            cost += Math.abs(m - c);
        }
        else { // "step"
            cost += Math.abs(m - c) * (Math.abs(m - c) + 1) / 2;
        }
    }
    return cost;
}

function min_fuel_cost(positions, method) {
    var m = median(positions);
    var cost = {};
    cost[m] = fuel_cost(positions, m, method);
    cost[m-1] = fuel_cost(positions, m-1, method);
    cost[m+1] = fuel_cost(positions, m+1, method);
    var n = (cost[m-1] < cost[m]) ? m-1 : (cost[m+1] < cost[m]) ? m+1 : m;
    if (n === m) return cost[m];
    var incr = (n === m-1) ? -1 : +1;
    var prev = m;
    while (cost[n] < cost[prev]) {
        prev = n;
        n += incr;
        cost[n] = fuel_cost(positions, n, method);
    }
    return cost[prev];
}

function part1(pi) {
    var positions = pi.split(',').map(Number);
    var ans = min_fuel_cost(positions, "constant");
    console.log(`part1: ${ans}`);
}

function part2(pi) {
    var positions = pi.split(',').map(Number);
    var ans = min_fuel_cost(positions, "step");
    console.log(`part2: ${ans}`);
}

console.log("day07");
var f = fs.readFileSync('aoc2021_day07.txt', 'utf8');
var pi = f.toString();
part1(pi);
part2(pi);