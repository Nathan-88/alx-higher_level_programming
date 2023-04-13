#!/usr/bin/node
//  a script that prints x times “C is fun”
//  Where x is the first argument of the script
//  If the first argument can’t be converted to an integer, print “Missing number of occurrences”
//  You must use console.log(...) to print all output
//  You are not allowed to use var
const args = process.argv;
if (args.length === 3 && !isNaN(args[2])) {
    for (let i = 0; i < parseInt(args[2]); i++) {
        console.log('C is fun');
    }
    }
else {
    console.log('Missing number of occurrences');
}
