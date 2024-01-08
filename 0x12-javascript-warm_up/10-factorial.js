#!/usr/bin/node

const x = parseInt(process.argv[2]);

function factorial (a) {
  if (a === 1) {
    return a;
  }
  return a * factorial(a - 1);
}
if (x) {
  console.log(factorial(x));
} else {
  console.log(1);
}
