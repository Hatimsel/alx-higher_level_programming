#!/usr/bin/node

const x = process.argv[2];

if (parseInt(x)) {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
