#!/usr/bin/node
/**
 *  a script that imports an array and computes a new array
 */
const list = require('./100-data').list;

const newList = list.map((x, i) => x * i);
console.log('Initial list:', list);
console.log('New list:', newList);
