#!/usr/bin/node
// Turn a String into Number
const args = process.argv.slice(2);
const toNumber = parseInt(args[0]);

if (toNumber) {
  console.log('My number:', toNumber);
} else {
  console.log('Not a number');
}
