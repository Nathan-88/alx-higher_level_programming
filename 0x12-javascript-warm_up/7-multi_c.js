#!/usr/bin/node
//  a script that prints x times “C is fun”
const length = process.argv[2];
if (!isNaN(length)) {
  for (let i = 0; i < length; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
