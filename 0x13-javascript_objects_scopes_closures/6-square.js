#!/usr/bin/node

const ParentSquare = require("./5-square.js");

class Square extends ParentSquare {
  charPrint(c) {
    c = c ? c : "X";
    for (let i = 0; i < this.height; i++) {
      let element = "";
      for (let j = 0; j < this.width; j++) {
        element += c;
      }
      console.log(element);
    }
  }
}
module.exports = Square;
