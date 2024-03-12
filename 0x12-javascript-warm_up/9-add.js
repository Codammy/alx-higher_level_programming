#!/usr/bin/node

const argv = require('process').argv;
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(a, b);
