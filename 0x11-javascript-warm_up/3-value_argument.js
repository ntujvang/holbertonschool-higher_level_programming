#!/usr/bin/node
// Script that prints first argument passed
if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
