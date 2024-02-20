#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const peopleUrl = url.replace('/films', '/people/18');

request(peopleUrl, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const result = JSON.parse(body);
    console.log(result.films.length);
  }
});
