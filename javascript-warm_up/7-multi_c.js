#!/usr/bin/node
// Print x times 'C is fun'
const args = process.argv.slice(2);
const toNumber = parseInt(args);

if (toNumber) {
  for (let cnt = 0; cnt < toNumber; cnt++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
