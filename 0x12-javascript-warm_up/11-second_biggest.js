#!/usr/bin/node
//  a script that searches the second biggest integer in the list of arguments.
// You can assume all arguments can be converted to integer
// if no argument passed, print 0
// If the number of arguments is 1, print 0
// You must use console.log(...) to print all output
const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const nums = args.map(arg => parseInt(arg));
  const sortedNums = nums.sort((a, b) => b - a);
  console.log(sortedNums[1]);
}
