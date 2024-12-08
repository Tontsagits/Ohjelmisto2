'use strict';

// alustetaan lista ja apumuuttuja
const numbers = [];
let number = 0;

// kysytään numeroita, kunnes input jo annettu numero
while (true) {
  number = parseInt(
      prompt(`Anna numero (jo annettu numero lopettaa)`, 'Numero tähän.'));
  if (numbers.includes(number)) {
    break;
  }
  // lisätään annetut numerot listaan
  numbers.push(number);
}

// järjestetään numerot pienimmästä suurimpaan
numbers.sort((a, b) => a - b);

// tulostetaan numerot konsoliin
for (let number of numbers) {
  console.log(number);
}
