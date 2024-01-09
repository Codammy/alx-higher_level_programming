#!/usr/bin/node
const { argv, stdout } = require('process');
const size = Number(argv[2]);
if (size) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) { stdout.write('X'); }
    console.log();
  }
} else { console.log('Missing size'); }
