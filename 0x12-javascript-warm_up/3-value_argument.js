#!/usr/bin/node

const arrArgs = process.argv;

if (arrArgs[2]) {
  console.log(arrArgs[2]);
} else {
  console.log('No argument');
}
