#!/usr/bin/node
// a script that computes and prints a factorial
// The first argument is integer (argument can be cast as integer) used for computing the factorial
// Factorial of NaN is 1
// You must do it recursively
// You must use a function
// You must use console.log(...) to print all output

function factorial (n) {
  if (isNaN(parseInt(n))) {
    return 1;
  } else if (parseInt(n) === 0) {
    return 1;
  } else {
    return parseInt(n) * factorial(parseInt(n) - 1);
  }
}

const input = process.argv[2];
const result = factorial(input);

console.log(result);
