#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { this.print(); } else {
      for (let h = 0; h < this.height; h++) {
        for (let w = 0; w < this.width; w++) { process.stdout.write(c); }
        console.log();
      }
    }
  }
}
module.exports = Square;
