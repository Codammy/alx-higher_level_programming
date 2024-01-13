#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  len--;
  const newL = [];
  while (list[len]) {
    newL.push(list[len]);
    len--;
  }
  return (newL);
};
