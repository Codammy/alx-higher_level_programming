exports.nbOccurences = function (list, searchElement) {
  nbOccur = 0;
  list.forEach((element) => {
    if (searchElement === element) {
      nbOccur++;
    }
  });
  return nbOccur;
};
