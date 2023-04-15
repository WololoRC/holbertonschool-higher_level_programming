#!/usr/bin/node

const args = process.argv.slice(2);
const output = ['No argument', 'Argument found', 'Arguments found'];

if (args.length <= 1) {
  console.log(output[args.length]);
} else {
  console.log(output[2]);
}
