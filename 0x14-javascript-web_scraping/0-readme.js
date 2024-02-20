#!/usr/bin/node
const fs = require('node:fs');

if (process.argv.length < 3) {
  console.log('Usage: ./0-readme.js file_path');
} else {
  fs.readFile(process.argv[2], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}
