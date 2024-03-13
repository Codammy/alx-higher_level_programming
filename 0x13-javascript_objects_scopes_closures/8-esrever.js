#!/usr/bin/node

exports.esrever = function (list) {
  let rev = [];
  list.forEach((element) => {
    rev.unshift(element);
  });
  return rev;
};
