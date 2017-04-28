#!/usr/bin/node
// Script that prints 'My number' if first argv can can be int
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
