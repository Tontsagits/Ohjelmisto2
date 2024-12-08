'use strict';

const n1 = parseInt(prompt('Anna ensimmäinen numero:', 'Numero tähän.'));
const n2 = parseInt(prompt('Anna toinen numero:', 'Numero tähän.'));
const n3 = parseInt(prompt('Anna kolmas numero:', 'Numero tähän.'));
const n4 = parseInt(prompt('Anna neljäs numero:', 'Numero tähän.'));
const n5 = parseInt(prompt('Anna viides numero:', 'Numero tähän.'));

const numbers = [n1, n2, n3, n4, n5];
let numbersStr = ``;

for (let i = numbers.length; i > 0; i--) {
  console.log(numbers[i - 1]);
  numbersStr += `${numbers[i - 1]}, `;
}

numbersStr = numbersStr.slice(0, -2);

document.querySelector(
    '#tag1').innerHTML = `Numbers in reverse order: ${numbersStr}`;
