#!/usr/bin/node
// Defines a Square object who inherits from Rectangle

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (w) {
    super(w, w);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let cnt = 0; cnt < this.width; cnt++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
