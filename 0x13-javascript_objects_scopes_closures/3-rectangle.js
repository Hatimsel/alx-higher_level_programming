#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    while (this.height > 0) {
      let i = this.width;
      while (i > 0) {
        process.stdout.write('X');
        // console.log('X');
        i--;
      }
      console.log();
      this.height--;
    }
  }
};
