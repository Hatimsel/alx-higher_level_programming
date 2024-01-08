#!/usr/bin/node

const numArgs = process.argv.length;
if (numArgs <= 3) {
  console.log(0);
} else {
  const arrArgs = toInt(process.argv);
  console.log(arrArgs.sort()[numArgs - 2]);
}

function toInt (arr) {
  let i = 0;
  const length = arr.length;

  while (i < length) {
    parseInt(arr[i]);
    i++;
  }
  return arr;
}
