#!/usr/bin/node
const list = require('./100-data').list;
let c = 0;
const newList = list.map((i) => { return (i * [c++]); });

console.log(list);
console.log(newList);
