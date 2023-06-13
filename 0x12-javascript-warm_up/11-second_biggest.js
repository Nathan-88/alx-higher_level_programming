#!/usr/bin/node
//  a script that searches the second biggest integer in the list of arguments.
const num = process.argv;
const new_num = [];
if (num.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < num.length; i++) {
    new_num.push(parseInt(num[i]));
  }
  new_num.sort(function (a, b) { return a - b; });
  console.log(new_num[new_num.length - 2]);
}
