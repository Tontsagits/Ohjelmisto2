'use strict';

let result = 0;
let numbers = [];

const butTE = document.querySelector('#start');
const pTE = document.querySelector('#result');

butTE.addEventListener('click', function() {
  const calculation = document.querySelector('#calculation').value;
  console.log(calculation);
  if (calculation.includes('+')) {
    numbers = calculation.split('+');
    result = parseInt(numbers[0]) + parseInt(numbers[1]);
  } else if (calculation.includes('-')) {
    numbers = calculation.split('-');
    result = parseInt(numbers[0]) - parseInt(numbers[1]);
  } else if (calculation.includes('*')) {
    numbers = calculation.split('*');
    result = parseInt(numbers[0]) * parseInt(numbers[1]);
  } else if (calculation.includes('/')) {
    numbers = calculation.split('/');
    result = parseInt(numbers[0]) / parseInt(numbers[1]);
  }
  pTE.innerHTML = `${result}`;
});
