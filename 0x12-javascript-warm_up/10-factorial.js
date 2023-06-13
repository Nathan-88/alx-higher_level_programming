#!/usr/bin/node
// a script that computes and prints a factorial

function factorial (num) {
  if (isNaN(num) === NaN || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
