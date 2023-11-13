#!/usr/bin/node

if (process.argv[2]) {
  if (parseInt(process.argv[2])) {
    const times = parseInt(process.argv[2]);
    let i = 0;
    while (i < times) {
      console.log('C is fun');
      i += 1;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
