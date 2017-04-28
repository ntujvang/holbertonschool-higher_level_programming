#!/usr/bin/node
// Script that x times 'C is fun'
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
}
for (let i = 0; i < Number(process.argv[2]); i++) {
  console.log('C is fun');
}
