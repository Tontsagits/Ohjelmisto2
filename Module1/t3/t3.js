'use strict';

alert('Anna kolme kokonaislukua!');

const n1 = parseInt(
    prompt('Eka numero:', 'Eka numero.'));
const n2 = parseInt(
    prompt('Toka numero:', 'Toka numero.'));
const n3 = parseInt(
    prompt('Kolmas numero:', 'Kolmas numero.'));

const sum = n1 + n2 + n3;
const prod = n1 * n2 * n3;
const avg = (n1 + n2 + n3) / 3;
document.querySelector(
    '#tag1').innerHTML = `Sum of numbers ${n1}, ${n2} and ${n3} is ${sum}.`;
document.querySelector(
    '#tag2').innerHTML = `Product of numbers ${n1}, ${n2} and ${n3} is ${prod}.`;
document.querySelector(
    '#tag3').innerHTML = `Avarage of numbers ${n1}, ${n2} and ${n3} is ${avg}.`;
