#!/usr/bin/node

let numberOfCall = 0;
exports.logMe = function (item) {
  console.log(numberOfCall + ': ' + item);
  numberOfCall++;
};
