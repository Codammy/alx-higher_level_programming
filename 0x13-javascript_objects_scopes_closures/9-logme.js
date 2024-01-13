#!/usr/bin/node
let n = 0;
exports.logMe = function (item) {
  console.log('%d: %s', n, item);
  n++;
};
