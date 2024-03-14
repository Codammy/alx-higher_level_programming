#!/usr/bin/node

const argv = require('process').argv;
const list = argv.splice(2);

if (!list || !list[1]) {
  console.log(0);
} else {
  let secondBiggest;
  let biggest = list[0];
  for (let i = 0; i < list.length; i++) {
    if (list[i] > biggest) {
      biggest = list[i];
    }
  }

  secondBiggest = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] < biggest && list[i] >= secondBiggest) {
      secondBiggest = list[i];
    }
  }
  console.log(secondBiggest);
}
