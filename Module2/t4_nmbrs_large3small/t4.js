'use strict';

// alustetaan lista ja apumuuttuja
const numbers = [];
let number = 0;

// kysytään numeroita, kunnes input on nolla
while (true) {
  number = parseInt(prompt(`Anna numero (0 lopettaa)`, 'Numero tähän.'));
  if (number === 0) {
    break;
  }
  // lisätään annetut numerot listaan
  numbers.push(number);
}

// järjestetään numerot pienimmästä suurimpaan
numbers.sort((a, b) => a - b);
// käännetään järjestys
numbers.reverse();

// tulostetaan numerot konsoliin
for (let number of numbers) {
  console.log(number);
}
