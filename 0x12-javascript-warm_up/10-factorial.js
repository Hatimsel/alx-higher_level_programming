#!/usr/bin/node

function factorial (x) {
  let result = x;
  while (x > 1) {
    result *= x - 1;
    x -= 1;
  }
  console.log(result);
}
const x = parseInt(process.argv[2]);

factorial(x);
