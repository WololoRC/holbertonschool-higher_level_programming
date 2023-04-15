#!/usr/bin/node
// Print the second biggest number
let args = process.argv.slice(2);

for (let cnt = 0; cnt < args.length; cnt++) {
  args[cnt] = parseInt(args[cnt]);
}

args.sort(function (a, b) {
  return b - a;
});

args = args[1];

if (!args) {
  args = 0;
}

console.log(args);
