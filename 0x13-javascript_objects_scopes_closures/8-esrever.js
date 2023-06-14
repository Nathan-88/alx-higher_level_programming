#!/usr/bin/node
//  a function that returns the reversed version of a list
exports.esrever = function (list) {
  const newlist = [];
  for (let i = 0; i < list.length; i++) {
    newlist.unshift(list[i]);
  }
  return newlist;
};
