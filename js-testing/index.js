'use strict';

// Konsoli

console.log('Hello Javascript World!');

// Muuttuja

let muuttuja;
muuttuja = 'Hank Moody';
console.log(muuttuja);

// Vakio

const vakio = 'Another Hank Moody';
console.log(vakio);

// alert popup

alert('Hello JavaScript World from here too!');

// Kysytään tietoja promptilla

const name = prompt('Anna nimesi:', 'Nimi tähän.');
document.querySelector('#testingpara1').innerHTML = 'Hello, ' + name + '!';

const answer = confirm('No miten on? Kyllä vai ei?');
console.log(answer);
console.log(typeof answer);

// string vai numero

const ageInt = parseInt(prompt('Anna ikäsi:', 'Ikä tähän.'));
console.log(ageInt);
console.log(typeof ageInt);

// Muuttujia

let first, second, third, all;
first = 'Good ';
second = 'morning ';
third = 'all.';
all = first + second + third;
console.log(all);

const nameToo = 'Mr. Skywalker';
const greeting = `Hello, ${nameToo}`;
document.querySelector('#testingpara2').innerHTML = greeting;

//  operaattoreita

let number = 3;
number = number * 7;     // the value is now 21
number = 1 + number / 2;   // the value is now 11.5
console.log(number);

//  operaattoreita

number = 3;
number++;     // the value is now 4
console.log(number);
number--;     // the value is again 3
console.log(number);

// Matematiikka objekti

console.log(Math.sqrt(3));
console.log(Math.random());

// määrätyt vakiot Designated Constants

const multiplier = 4.1868;
const k1 = prompt('Give the amount of energy for lunch (kcal).');
const k2 = prompt('Enter the amount of energy for dinner(kcal).');

const j1 = multiplier * k1;
const j2 = multiplier * k2;

console.log(`At breakfast you got ${j1} kJ and at dinner you got ${j2} kJ.`);

