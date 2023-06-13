#!/usr/bin/node
//  a script that searches the second biggest integer in the list of arguments.
const num = process.argv;
const List = [];
if (num.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < num.length; i++) {
    List.push(parseInt(num[i]));
  }
  List.sort(function (a, b) { return a - b; });
  console.log(List[List.length - 2]);
}
