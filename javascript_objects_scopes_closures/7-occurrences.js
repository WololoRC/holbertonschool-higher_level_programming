#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let cnt = 0; cnt < list.length; cnt++) {
    if (list[cnt] === searchElement) {
      count += 1;
    }
  }
  return count;
};
