#!/usr/bin/node
const { argv } = require('process');
const len = argv.length;
let big;

if (len < 4) { console.log(0); } else {
  let n = 0;
  while (n < len) {
    for (let i = len - 1; i > 2; i--) {
      if (Number(argv[i]) > Number(argv[i - 1])) {
        big = argv[i];
        argv[i] = argv[i - 1];
        argv[i - 1] = big;
      }
    }
    n++;
  }
  console.log(argv[3]);
}
