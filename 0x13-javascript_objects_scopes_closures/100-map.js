#!/usr/bin/node

const list = require('./100-data.js').list;

const arr = list.map((x) => x * list.indexOf(x));

console.log(list);
console.log(arr);
