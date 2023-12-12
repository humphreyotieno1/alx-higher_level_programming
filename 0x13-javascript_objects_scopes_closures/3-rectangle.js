#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let a = 0; a < this.height; a += 1) {
      console.log('X'.repeat(this.width));
    }
  }
};
