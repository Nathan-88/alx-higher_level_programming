#!/usr/bin/node
// a function that executes x times a function.
// The function must be visible from outside
// Prototype: function (x, theFunction)
function executeNTimes(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports.executeNTimes = executeNTimes