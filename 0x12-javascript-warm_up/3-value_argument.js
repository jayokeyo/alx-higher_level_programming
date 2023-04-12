#!/usr/bin/node
/*
 * Use console.log to print first argument passed to function
 */
let firstArgument = process.argv[2];
console.log(firstArgument === undefined ? 'No argument' : firstArgument);
