#!/usr/bin/node

const ParentSquare = require('./5-square.js');
module.exports = class Square extends ParentSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
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
