#!/usr/bin/node
// Script that prints 3 lines but uses array
const myArray = new Array(3);
myArray[0] = 'C is fun';
myArray[1] = 'Python is cool';
myArray[2] = 'Javascript is amazing';
for (let i = 0; i < myArray.length; i++) {
  console.log(myArray[i]);
}
