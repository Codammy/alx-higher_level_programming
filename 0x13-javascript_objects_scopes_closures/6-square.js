#!/usr/bin/node
const stdout = require('process').stdout;
const pSquare = require('./5-square');

class Square extends pSquare {
  charPrint (c) {
    c = c || 'X';
    const w = this.width;
    const h = this.height;
    for (let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        stdout.write(c);
      }
      console.log('');
    }
  }
}
module.exports = Square;
