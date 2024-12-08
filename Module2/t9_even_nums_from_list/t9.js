'use strict';

function even(array) {
  const evenNumbers = [];
  for (let numero of array) {
    if (numero % 2 === 0) {
      evenNumbers.push(numero);
    }
  }
  return evenNumbers;
}

const numerot = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10,
  11,
  12,
  13,
  14,
  15,
  16,
  17,
  18,
  19,
  20,
  21,
  22,
  23,
  24,
  25];

const parillisetNumerot = even(numerot);

console.log(numerot);
console.log(parillisetNumerot);
