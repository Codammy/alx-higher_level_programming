#!/usr/bin/node
const num = require('process').argv[2];
function factorial (n) {
  if (n === 1 || !n) { return (1); }
  return (n * factorial(n - 1));
}
console.log(factorial(Number(num)));
