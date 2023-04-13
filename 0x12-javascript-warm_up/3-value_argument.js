#!/usr/bin/node
// a script that prints the first argument passed to it:
// If no arguments are passed to the script, print “No argument”
const args = process.argv;
if (args.length === 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
