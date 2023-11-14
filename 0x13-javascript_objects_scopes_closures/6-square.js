#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c !== undefined) {
      let i = this.height;
      while (i > 0) {
        let j = this.width;
        while (j > 0) {
          process.stdout.write(c);
          j--;
        }
        console.log();
        i--;
      }
    } else {
      this.print();
    }
  }
};
