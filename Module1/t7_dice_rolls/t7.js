'use strict';

const number = parseInt(prompt('How many rolls of dice?', 'Number here.'));

let rndmNmbr = 0;
let sum = 0;
let rndmNmbrStr = '';

for (let i = 1; i <= number; i++) {
  rndmNmbr = Math.floor(Math.random() * 6);
  sum += rndmNmbr;
  rndmNmbrStr += `${rndmNmbr}, `;
}

const numbersStr = rndmNmbrStr.slice(0, -2);

document.querySelector(
    '#tag1').innerHTML = `The sum of ${number} rolls of dice (${numbersStr}) is ${sum}`;
