#!/usr/bin/node
const list = require('./100-data').list;
let index = -1;
const newList = list.map(item => {
  index++;
  return (item * index);
});
console.log(list, newList);
