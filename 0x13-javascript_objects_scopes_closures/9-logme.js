#!/usr/bin/node
let nPrinted = 0;
exports.logMe = function (item) {
  console.log(`${nPrinted++}: ${item}`);
};
