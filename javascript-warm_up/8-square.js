#!/usr/bin/node
// Print a square'
const args = process.argv.slice(2);
const toNumber = parseInt(args);

if (toNumber) {
  for (let cnt = 0; cnt < toNumber; cnt++) {
    console.log('X'.repeat(toNumber));
  }
} else {
  console.log('Missing size');
}
