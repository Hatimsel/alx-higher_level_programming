#!/usr/bin/node

if (process.argv[2]) {
  if (parseInt(process.argv[2])) {
    const times = parseInt(process.argv[2]);
    let x = 0;
    while (x < times) {
      let y = 0;
      while (y < times) {
        // console.log(`X`);
        process.stdout.write('X');
        y += 1;
      }
      console.log();
      x += 1;
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
