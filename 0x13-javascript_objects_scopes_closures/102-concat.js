#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, (err, data) => {
  if (err) throw err;
  fs.writeFile(fileC, data, (err) => {
    if (err) throw err;
  });
});
fs.readFile(fileB, (err, data) => {
  if (err) throw err;
  fs.appendFile(fileC, data, (err) => {
    if (err) throw err;
  });
});
