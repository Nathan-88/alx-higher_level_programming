#!/usr/bin/node
//  a function that executes x times a function
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
