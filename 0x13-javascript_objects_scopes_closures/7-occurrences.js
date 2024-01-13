#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let app = 0;
  for (const i of list) {
    if (i === searchElement) { app++; }
  }
  return (app);
};
