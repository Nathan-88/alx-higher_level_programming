#!/usr/bin/node
// a script that computes and prints a factorial

function factorial(num) {
    if (num === 0 || num === 1) {
        return 1;
    }
    return num * factorial(num - 1);
}
num = parseInt(process.argv[2]);
console.log(factorial(num));