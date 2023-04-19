#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

request(args[0], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  const catchedBody = JSON.parse(body).results;
  let cnt = 0;
  // for each item in @results
  for (const n in catchedBody) {
    if (catchedBody[n].characters.find(item => item.endsWith('/18/'))) {
      cnt++;
    }
  }
  console.log(cnt);
});
