#!/usr/bin/node
// Script that prints a square of size argv[2]
if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
for (let y = 0; y < process.argv[2]; y++) {
  console.log('X'.repeat(process.argv[2]));
}
