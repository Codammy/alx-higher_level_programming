#!/usr/bin/node
exports.callMeMoby = function (t, func) {
  let n = 0;
  while (n < t) {
    func();
    n++;
  }
};
