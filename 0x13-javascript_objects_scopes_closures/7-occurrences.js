#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nbOccur = 0;
  list.forEach((element) => {
    if (searchElement === element) {
      nbOccur++;
    }
  });
  return nbOccur;
};
