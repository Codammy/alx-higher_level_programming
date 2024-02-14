#!/usr/bin/node
const { argv, stdout } = require('process');
const num = Number(argv[2]);
if (!num) {
  console.log('Missing size');
} else {
  let i, j;
  for (i = 0; i < num; i++) {
    for (j = 0; j < num; j++) {
      stdout.write('X');
    }
    console.log('');
  }
}
