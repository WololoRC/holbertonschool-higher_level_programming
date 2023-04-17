#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/people/18/', function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const count = JSON.parse(body);
  console.log(count.films.length);
});
