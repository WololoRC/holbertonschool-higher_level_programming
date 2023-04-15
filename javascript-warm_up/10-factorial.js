#!/usr/bin/node
// Prints the addition of 2 integers
let args = process.argv.slice(2);

args = parseInt(args[0]);
if (!args) {
  args = 1;
}

function toFactorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * toFactorial(n - 1);
  }
}

console.log(toFactorial(args));
