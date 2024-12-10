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
  /*
  const num1 = parseInt(document.querySelector('#num1').value);
  const num2 = parseInt(document.querySelector('#num2').value);
  if (option === 'add') {
    result = num1 + num2;
  } else if (option === 'sub') {
    result = num1 - num2;
  } else if (option === 'multi') {
    result = num1 * num2;
  } else if (option === 'div') {
    result = num1 / num2;
  }
  */
  pTE.innerHTML = `${result}`;
});
