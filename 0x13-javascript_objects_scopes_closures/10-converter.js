#!/usr/bin/node
exports.converter = function (base) {
  return (n) => parseInt(n, 10).toString(base);
};
