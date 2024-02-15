#!/usr/bin/node
const { dict } = require('./101-data');
const newDict = {};
for (const id in dict) {
  const occ = dict[id];
  if (newDict[occ]) {
    const arr = newDict[occ];
    arr.push(id);
    continue;
  }
  newDict[occ] = Array(id);
}
console.log(newDict);
