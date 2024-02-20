#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (err, resp) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', resp && String(resp.statusCode));
  }
});
