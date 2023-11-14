#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let h = this.height;
    while (h > 0) {
      let i = this.width;
      while (i > 0) {
        process.stdout.write('X');
        // console.log('X');
        i--;
      }
      console.log();
      h--;
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
