#!/usr/bin/node
/* a script that concats 2 files
The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination
*/
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const textA = fs.readFileSync(fileA, 'utf8');

const textB = fs.readFileSync(fileB, 'utf8');

const newText = `${textA}${textB}`;
fs.writeFileSync(fileC, newText);
