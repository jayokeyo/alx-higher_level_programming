#!/usr/bin/node
/*
 * Use console.log to print different messages
 * depending on number of arguments passed
 */
const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
