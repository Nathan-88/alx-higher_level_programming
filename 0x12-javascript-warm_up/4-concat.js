#!/usr/bin/node
// a script that prints two arguments passed to it, in the following format: “ is ”
// You must use console.log(...) to print all output
// You are not allowed to use var
const args = process.argv;
if (args.length === 2) {
    console.log('undefined is undefined');
    }
else if (args.length === 3) {
    console.log(args[2] + ' is undefined');
    }
else {
    console.log(args[2] + ' is ' + args[3]);
    }
