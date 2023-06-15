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
// read from file A and store in variable "textA"
// console.log("File A: ", textA); //print out File A to console for debugging purposes
const textB = fs.readFileSync(fileB, 'utf8');
// read from file B and store in variable "textB"
// console.log("File B: ", textB); //print out File B to console for debugging purposes
const newText = `${textA}\n${textB}`;
// concatenate textA and textB and store in variable "newText"
// console.log("New Text: ", newText); //print out New Text to console for debugging purposes
fs.writeFileSync(fileC, newText);
// write newText to fileC
// console.log("File C: ", fileC); //print out File C to console for debugging purposes
