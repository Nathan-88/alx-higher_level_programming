#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return 'Rectangle {}';
    }
  }

  // print rectangle
  print () {
    if (this.width < 1 || this.height < 1) {
      return {};
    }

    for (let i = 1; i <= this.height; i++) {
      let row = '';
      for (let j = 1; j <= this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  // rotate() exchanges the width and the height of the rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // double() that multiples the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
