#!/usr/bin/node
const fs = require('node:fs');

if (process.argv.length < 4) {
  console.log('Usage: ./0-readme.js file_path string to write');
} else {
  fs.writeFile(process.argv[2], process.argv[3], (err) => {
    if (err) {
      console.error(err);
    } else {
      // file written succefully
    }
  });
}
