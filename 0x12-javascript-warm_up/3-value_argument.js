#!/usr/bin/node
let firstArgument = process.argv[2];
console.log(firstArgument === undefined ? 'No argument' : firstArgument);
