let n = 10,
    n1 = 0 // n1：最大能达第 n1 个菱形的
if (n === 0) {
    console.log('剩余*:0');
    return;
}
if (n === 1) {
    console.log('*');
    console.log('剩余*:0');
    return;
}
let total = 0
while (total <= n) {
    n1++;
    total = 2 * Math.pow(n1 - 1, 2) + 2 * n1 - 1;
}
n1--;
total = 2 * Math.pow(n1 - 1, 2) + 2 * n1 - 1;

let ans2 = n - total;
let ans1 = '';
for (let i = 1; i <= n1; i++) {
    for (let j = 1; j <= n1 - i; j++) {
        ans1 += ' ';
    }
    for (let j = 1; j <= 2 * i - 1; j++) {
        ans1 += '*';
    }
    ans1 += '\n';
}
n1--;
for (let i = 1; i <= n1; i++) {
    for (let j = 1; j <= i; j++) {
        ans1 += ' ';
    }
    for (let j = 1; j <= (2 * n1 - 1) + (-2 * i + 2); j++) {
        ans1 += '*';
    }
    if (i != n1) {
        ans1 += '\n';
    }
}
console.log(ans1);
console.log(`剩余*:${ans2}`);