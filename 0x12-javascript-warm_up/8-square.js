#!/usr/bin/node

const argv = require('process').argv;
const number = parseInt(argv[2]);
let c = number * number;
let str = '';
if (!number) { console.log('Missing size'); } else {
  while (c > 0) {
    str += 'X';
    c--;
    if ((c % number === 0) && c !== 0) {
      str += '\n';
    }
  }
  console.log(str);
}
