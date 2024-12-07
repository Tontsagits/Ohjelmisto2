'use strict';

const choise = confirm('Should I calculate the square root?');

if (choise) {
  const number = parseInt(
      prompt('Anna numero (kokonaisluku):', 'Numero tähän.'));
  if (number < 0) {
    document.querySelector(
        '#tag1').innerHTML = `The square root of a negative number is not defined.`;
  } else {
    document.querySelector(
        '#tag1').innerHTML = `Square root of ${number} is ${Math.sqrt(number)}`;
  }
} else {
  document.querySelector(
      '#tag1').innerHTML = `The square root is not calculated.`;
}
