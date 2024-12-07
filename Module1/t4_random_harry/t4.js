'use strict';

const name = prompt('Anna nimesi:', 'Nimesi tähän.');

let hwClass;

const rndValue = Math.floor(Math.random() * 4);

// Select of houses Gryffindor, Slytherin, Hufflepuff, and Ravenclaw.

if (rndValue === 1) {
  hwClass = 'Gryffindor';
} else if (rndValue === 2) {
  hwClass = 'Slytherin';
} else if (rndValue === 3) {
  hwClass = 'Hufflepuff';
} else if (rndValue === 4) {
  hwClass = 'Ravenclaw';
}

document.querySelector(
    '#tag1').innerHTML = `${name}, you are a ${hwClass}.`;
