#!/usr/bin/node
// a script that prints the first argument passed to it
const arg = process.argv;

const result = (arg.length === 2) ? 'No argument' : arg[2];
console.log(result);
