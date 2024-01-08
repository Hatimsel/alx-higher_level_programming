#!/usr/bin/node

const numArgs = process.argv.length;

if (numArgs > 3) {
  console.log('Not a number');
} else {
  if (parseInt(process.argv[2])) {
    console.log('My number: %d', parseInt(process.argv[2]));
  } else {
    console.log('Not a number');
  }
}
