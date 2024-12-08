'use strict';

const someIntNumber = parseInt(
    prompt('Anna positiivinen kokonaisluku:', 'Numero tähän.'));

// alussa oletetaan että on alkuluku

let isPrime = true;

// jos jakolasku itseään pienemmällä menee tasan niin ei ole alkuluku

for (let i = 2; i < someIntNumber; i++) {
  if (someIntNumber % i === 0) {
    isPrime = false;
  }
}

if (isPrime) {
  document.querySelector('#tag1').innerHTML = `${someIntNumber} on alkuluku.`;
} else {
  document.querySelector(
      '#tag1').innerHTML = `${someIntNumber} ei ole alkuluku.`;
}
