#!/usr/bin/node
// a class Rectangle that defines a rectangle

// You must use the class notation for defining your class
// The constructor must take 2 arguments: w and h
// Initialize the instance attribute width with the value of w
// Initialize the instance attribute height with the value of h
// If w or h is equal to 0 or not a positive integer, create an empty object
// Create an instance method called print() that prints the rectangle using the character X

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (this.width < 1 || this.height < 1) {
      return {};
    }

    for (let i = 1; i <= this.height; i++) {
      // let row = "";
      for (let j = 1; j <= this.width; j++) {
        process.stdout.write('X');
      }
      console.log('');
      // console.log(row);
    }
  }
}

module.exports = Rectangle;
