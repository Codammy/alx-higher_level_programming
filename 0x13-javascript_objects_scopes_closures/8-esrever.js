#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let l = list.length - 1; l >= 0; l--) {
    rev.push(list[l]);
  }
  return (rev);
};
