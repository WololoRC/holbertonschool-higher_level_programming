#!/usr/bin/node
// Defines a Rectangle wit Print method

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let cnt = 0; cnt < this.height; cnt++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }
}

module.exports = Rectangle;
