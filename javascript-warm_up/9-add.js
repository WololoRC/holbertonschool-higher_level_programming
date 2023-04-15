#!/usr/bin/node
// Prints the addition of 2 integers

const args = process.argv.slice(2);

for (let cnt = 0; cnt < args.length; cnt++) {
  args[cnt] = parseInt(args[cnt]);
}

console.log(args[0] + args[1]);
