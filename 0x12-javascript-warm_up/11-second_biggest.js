#!/usr/bin/node

const argv = require('process').argv;
const list = argv.splice(2);

if (!list || !list[1]) {
  console.log(0);
} else {
  let secondBiggest;
  let biggest = Number(list[0]);
  for (let i = 0; i < list.length; i++) {
    if (Number(list[i]) > biggest) {
      biggest = Number(list[i]);
    }
  }
  secondBiggest = 0;
  for (let i = 0; i < list.length; i++) {
    if (Number(list[i]) < biggest && Number(list[i]) >= secondBiggest) {
      secondBiggest = Number(list[i]);
    }
  }
  console.log(secondBiggest);
}
