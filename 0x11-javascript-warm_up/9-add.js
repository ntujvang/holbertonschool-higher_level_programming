#!/usr/bin/node
// Script that prints sum of 2 num
function add(a, b) {
  console.log(a + b);
}
add(Number(process.argv[2]), Number(process.argv[3]));
