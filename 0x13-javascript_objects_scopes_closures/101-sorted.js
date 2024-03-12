#!/usr/bin/node

const dict = require('./101-data').dict;
const newObj = {};
for (const k in dict) {
  const v = dict[k];
  if (newObj[v]) {
    newObj[v].push(k);
  } else {
    newObj[v] = [k];
  }
}
console.log(newObj);
