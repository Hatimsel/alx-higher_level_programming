#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (err, resp) => {
  console.log('code: ', resp && resp.statusCode);
});
