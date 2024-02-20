#!/usr/bin/node
const request = require('request');
const fs = require('node:fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(file, body, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
