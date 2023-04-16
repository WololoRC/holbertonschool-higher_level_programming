#!/usr/bin/node
// prints the number of arguments already printed and the new argument value

let cnt = 0;

exports.logMe = function (item) {
  console.log(cnt.toString(), ':', item);
  cnt++;
};
