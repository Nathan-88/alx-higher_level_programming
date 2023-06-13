#!/usr/bin/node
// script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const arg = process.argv;
const num = arg[2];
const integer = (!isNaN(num)) ? `My number: ${parseInt(num)}` : 'Not a number';

console.log(integer);
