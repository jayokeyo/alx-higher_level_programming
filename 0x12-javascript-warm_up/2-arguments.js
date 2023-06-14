#!/usr/bin/node
const argNumber = process.argv.length;
console.log(argNumber === 2 ? 'No argument': argNumber === 3 ? 'Argument found': 'Arguments found')
