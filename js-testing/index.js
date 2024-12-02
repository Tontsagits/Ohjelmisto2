'use strict';

console.log('Hello Javascript World!');

let muuttuja;
muuttuja = 'Hank Moody';
console.log(muuttuja);

const vakio = 'Another Hank Moody';
console.log(vakio);

alert('Hello JavaScript World from here too!');

const name = prompt('Anna nimesi:', 'Nimi tähän.');
document.querySelector('#testingpara').innerHTML = 'Hello, ' + name + '!';

const answer = confirm('No miten on? Kyllä vai ei?');
console.log(answer);
console.log(typeof answer);

const ageInt = parseInt(prompt('Anna ikäsi:', 'Ikä tähän.'));
console.log(ageInt);
console.log(typeof ageInt);

let first, second, third, all;
first = 'Good ';
second = 'morning ';
third = 'all.';
all = first + second + third;
console.log(all);
