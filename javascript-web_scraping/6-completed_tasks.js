#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const dict = {};

request(args[0], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }

  const catchBody = JSON.parse(body);

  catchBody.forEach((item) => {
    if (!dict[item.userId] && item.completed) {
      dict[item.userId] = 1;
    } else if (item.completed && dict[item.userId]) {
      dict[item.userId] += 1;
    }
  });

  console.log(dict);
});
