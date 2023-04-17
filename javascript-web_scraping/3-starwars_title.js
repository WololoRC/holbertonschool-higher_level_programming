#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request('https://swapi-api.alx-tools.com/api/films/' + args[0] + '/', function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  console.log(JSON.parse(body).title);
});
