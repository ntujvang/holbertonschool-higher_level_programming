#!/usr/bin/node
// Script that searches for second biggest int
let myArray = [];
let length = process.argv.length;
let big = null;
let bigger = null;
if (length <= 3) {
  console.log('0');
} else {
  for (let i = 0; (i + 2) < length; i++) {
    myArray[i] = (Number(process.argv[(i + 2)]));
  }
  myArray.sort();
  for (let i = 0; i < myArray.length; i++) {
    bigger = myArray[i];
    if (bigger < myArray[i + 1]) {
      big = bigger;
    }
  }
  console.log(big);
}
