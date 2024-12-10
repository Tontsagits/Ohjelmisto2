'use strict';

let result = 0;

const butTE = document.querySelector('#start');
const pTE = document.querySelector('#result');

butTE.addEventListener('click', function() {
  const option = document.querySelector('#operation').value;
  console.log(option);
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
  pTE.innerHTML = `${result}`;
});
