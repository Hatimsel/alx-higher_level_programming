#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let myList = process.argv.slice(2);
  for (let i = 0; i < myList.length; i++) {
    myList[i] = parseInt(myList[i]);
  }
  myList = (myList.sort(function (a, b) { return a - b; }));
  console.log(myList[myList.length - 2]);
}
