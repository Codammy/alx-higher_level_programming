#!/usr/bin/node
const proc = require('process').argv;
const num = Number(proc[2]);
if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < num; index++) {
    console.log('C is fun');
  }
}
