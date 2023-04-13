#!/usr/bin/node
//  a script that prints a square
// The first argument is the size of the square
// If the first argument can’t be converted to an integer, print “Missing size”
// You must use the character X to print the square
// You must use console.log(...) to print all output
// You are not allowed to use var
const args = process.argv;
if (args.length === 3 && !isNaN(args[2])) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log('X'.repeat(parseInt(args[2])));
  }
} else {
  console.log('Missing size');
}
