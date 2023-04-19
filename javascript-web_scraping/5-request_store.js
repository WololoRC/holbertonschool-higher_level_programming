#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const fs = require('fs');

request(args[0], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }

  fs.writeFile('./' + args[1], body, err => {
    if (err) {
      console.error(err);
    }
  });
});
