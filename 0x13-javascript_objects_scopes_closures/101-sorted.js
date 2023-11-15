#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
for (const key in dict) {
  const value = dict[key];
  if (value in Object.keys(newDict) === false) {
    newDict[value] = [];
    if (key in Object.values(newDict) === false) {
      newDict[value].push(key);
    } else {
      continue;
    }
  } else {
    if (key in Object.values(newDict) === false) {
      newDict[value].push(key);
    }
  }
}
console.log(newDict);
