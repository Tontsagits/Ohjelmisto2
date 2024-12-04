'use strict';

const yearNmbr = parseInt(prompt('Anna vuosiluku (nnnn):', 'Vuosiluku tähän.'));

if ((yearNmbr % 4 === 0 && yearNmbr % 100 !== 0) || (yearNmbr % 400 === 0)) {
  document.querySelector('#tag1').innerHTML = `${yearNmbr} is a leap year.`;
} else {
  document.querySelector('#tag1').innerHTML = `${yearNmbr} is NOT a leap year.`;
}
