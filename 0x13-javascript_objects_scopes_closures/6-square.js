#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (c) {
          process.stdout.write(c);
        } else {
          process.stdout.write('X');
        }
      }
      console.log();
    }
  }
};
