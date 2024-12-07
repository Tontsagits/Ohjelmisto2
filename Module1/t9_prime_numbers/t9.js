'use strict';

const startYear = parseInt(
    prompt('Anna aloitusvuosi (nnnn):', 'Vuosiluku tähän.'));
const endYear = parseInt(
    prompt('Anna lopetusvuosi (nnnn):', 'Vuosiluku tähän.'));

let inputStrToHtml = '';

/*
for (let i = startYear; i <= endYear; i++) {
  if ((i % 4 === 0 && i % 100 !== 0) || (i % 400 === 0)) {
    inputStrToHtml += `<li>${i}</li>`;
  } else {
    console.log(`${i} is NOT a leap year.`);
  }
  document.querySelector('#tag1').innerHTML = inputStrToHtml;
}
*/

