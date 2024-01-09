#!/usr/bin/node
const { argv } = require('process');
let occur = Number(argv[2]);
if (occur) {
  while (occur > 0) {
    console.log('C is fun');
    occur--;
  }
} else { console.log('Missing number of occurrences'); }
