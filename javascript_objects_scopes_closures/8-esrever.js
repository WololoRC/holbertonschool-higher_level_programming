#!/usr/bin/node
// Returns a reversed version of a list

exports.esrever = function (list) {
  const newList = [];

  let reverse = list.length - 1;

  for (let cnt = 0; cnt < list.length; cnt++) {
    newList.push(list[reverse]);
    reverse -= 1;
  }

  return newList;
};
