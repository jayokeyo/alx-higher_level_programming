#!/usr/bin/node
const input = parseInt(process.argv[2]);
console.log(isNaN(input) ? 'Not a number' : 'My number: ' + input);
