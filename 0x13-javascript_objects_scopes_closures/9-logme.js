#!/usr/bin/node
exports.logMe = function (item) {
  nPrinted = 0;
  const log = () => console.log(`${nPrinted++}: ${item}`);
  log();
};
