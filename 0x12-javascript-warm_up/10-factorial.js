#!/usr/bin/node
let fact = parseInt(process.argv[2]);
function Factorial (fact) {
  return fact === 0 || isNaN(fact) ? 1 : fact * Factorial(fact - 1);
}
console.log(Factorial(fact));
