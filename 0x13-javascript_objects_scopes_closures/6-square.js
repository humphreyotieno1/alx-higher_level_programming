#!/usr/bin/node
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let k = 0; k < this.width; k++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
