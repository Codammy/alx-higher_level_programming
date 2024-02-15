#!/usr/bin/node
const { argv } = require('process');
const arr = argv.slice(2);
for (let i = 0; i < arr.length; i++) {
  for (let j = arr.length - 1; j > 0; j--) {
    if (arr[j] > arr[j - 1]) {
      const tmp = arr[j];
      arr[j] = arr[j - 1];
      arr[j - 1] = tmp;
    }
  }
}
console.log(arr[1] ? arr[1] : arr[0]);
