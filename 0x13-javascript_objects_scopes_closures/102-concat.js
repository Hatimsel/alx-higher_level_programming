#!/usr/bin/node

const fs = require('fs');

const files = process.argv;

fs.readFile(files[2], (err, data) => {
  if (err) throw err;
  fs.writeFile(files[4], data, (err) => {
    if (err) throw err;
  });
});
fs.readFile(files[3], (err, data) => {
  if (err) throw err;
  fs.appendFile(files[4], data, (err) => {
    if (err) throw err;
  });
});
