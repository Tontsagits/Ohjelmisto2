'use strict';

// Konsoli

console.log('Hello Javascript World!');

//
//
//
// Muuttuja

let muuttuja;
muuttuja = 'Hank Moody';
console.log(muuttuja);

//
//
//
// Vakio

const vakio = 'Another Hank Moody';
console.log(vakio);

//
//
//
// alert popup

alert('Hello JavaScript World from here too!');

//
//
//
// Kysytään tietoja promptilla

const name = prompt('Anna nimesi:', 'Nimi tähän.');
document.querySelector('#testingpara1').innerHTML = 'Hello, ' + name + '!';

const answer = confirm('No miten on? Kyllä vai ei?');
if (answer) {
  console.log(`Nice! Your answer is ${answer}`);
} else {
  console.log(`Too bad your answer is ${answer}`);
}
console.log(answer);
console.log(typeof answer);

//
//
//
// string vai numero PARSE ja tulostus

const ageInt = parseInt(prompt('Anna ikäsi:', 'Ikä tähän.'));
if (ageInt < 30) {
  console.log(`Olet ${ageInt} vuotias nuori ihminen!`);
} else {
  console.log(`Olet ${ageInt} vuoden ikäinen aikuinen ihminen.`);
}
console.log(ageInt);
console.log(typeof ageInt);

//
//
//
// Muuttujia stringissä yhdistäminen

let first, second, third, all;
first = 'Good ';
second = 'morning ';
third = 'all.';
all = first + second + third;
console.log(all);

const nameToo = 'Mr. Skywalker';
const greeting = `Hello, ${nameToo}`;
document.querySelector('#testingpara2').innerHTML = greeting;

//
//
//
//  OPERAATTOREITA plus ja miinus

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

//
//
//
// Matematiikka objekti

console.log(Math.sqrt(3));
console.log(Math.random());
console.log(`Tässä numeron 3 neliöjuuri: ${Math.sqrt(3)}`);

//
//
//
// määrätyt vakiot Designated Constants

const multiplier = 4.1868;
const k1 = prompt('Give the amount of energy for lunch (kcal).');
const k2 = prompt('Enter the amount of energy for dinner(kcal).');

const j1 = multiplier * k1; // näköjään hyväksyy stringin sisällön kertoimeen
const j2 = multiplier * k2;

console.log(`At breakfast you got ${j1} kJ and at dinner you got ${j2} kJ.`);

//
//
//
// WHILE loop, tarkastus aina iteraatiota ENNEN eli ALUSSA while rivillä

let weight = prompt('Enter weight (kg) (must be positive).');
while (weight <= 0) {
  weight = prompt('The weight must be positive. Re-enter the weight (kg).');
}
console.log('You entered the weight: ' + weight + ' kg.');

// DO WHILE loops, TARKASTUS LOPUSSA eli WHILE rivillä

let result;
do {
  result = Math.floor(Math.random() * 6) + 1;
  console.log(result);
} while (result < 6);

// FOR loops

for (let i = 1; i <= 10; i++) {
  console.log(i);
}

// Nested FOR loops

let multiplication;
for (let i = 1; i <= 5; i++) {
  for (let j = 1; j <= 5; j++) {
    multiplication = i * j;
    console.log(i + ' times ' + j + ' is ' + multiplication + '.');
  }
}

//
//
//
// LIST ARRAYS

let numbers = []; // vakio, mutatoituva
numbers = [17, 2, 8];

const names = ['Frank', 'Scott', 'Jasmine', 'Don'];

for (let i = 0; i < names.length; i++) {
  console.log(`Name: ${names[i]}`);
}

for (let name of names) {
  console.log(`Name: ${name}`);
}

//
//
//
// OBJECT LITERALS (python dictionary)

const student = {
  firstName: 'Greg',
  lastName: 'Focker',
  studentId: '234359',
  phone: '040 5902123',
};

const greetings = `Hello, my name is ${student.firstName} ${student.lastName}`;
const studentInfo = `student number: ${student['studentId']}, phone number: ${student['phone']}`;
console.log(greetings);
console.log(studentInfo);

student.address = 'Schoolroad 7';  // adds 'address' property to previous example
delete student.phone;              // deletes 'phone' property from previous example

console.log(student);

const chosenProperty = 'lastName';
console.log(student[chosenProperty]);

//
//
//
// FUNKTIOT ilman paluuarvoa

function greet() {
  console.log('Well, hello!');
  return;
}

greet();

function greets(text, times) {
  for (let i = 1; i <= times; i++) {
    console.log(text + ' ' + i + '. time!');
  }
  return;
}

greets('Hi', 5);

//
//
//
// FUNKTIOT paluuarvoilla

function quadraticSum(first, second) {
  const result = first * first + second * second;
  return result;
}

const num1 = prompt('Enter 1. number.');
const num2 = prompt('Enter 2. number.');
const quad = quadraticSum(num1, num2);
console.log('The quadratic sum of ' + num1 + ' and ' + num2 + ' is ' + quad);

//
//
//
// GLOBAL vs LOCAL variables

const n1 = 3; // GLOBAL variable

function hello() {
  let n2 = 5; // an internal variable of a function

  if (n2 > 0) {
    const n3 = 8; // an internal variable of a block
    const n4 = 9; // an internal variable of a function
    console.log(n3);
    console.log(n4);
  }
  console.log(n1); // global variable is visible everywhere
  console.log(n2); // the internal variable is available inside the function
  //console.log(n3); -- an internal variable of a block is not available outside the function
  // console.log(n4); // the internal variable of the function is available inside the function
  return;
}

hello();

console.log(n1); // the global variable is visible everywhere
//console.log(n2); -- the function's internal variable does not appear outside the function
//console.log(n3); -- the internal variable of a block does not appear outside the block
//console.log(n4); -- the function's internal variable does not appear outside the function

//
//
//
// ARRAY as PARAMETER of a FUNCTION

function grow(array) {
  for (let i = 0; i < array.length; i++) {
    array[i]++;
  }
  return;
}

const numberz = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
grow(numberz);
console.log(numberz[0] + ' ' + numberz[1] + ' ' + numberz[2]);
for (let i = 0; i < numberz.length; i++) {
  console.log(`Listalla on luku: ${numberz[i]}`);
}

//
//
//
// LOTTO ARVONTA FUNKTIO JOKA LUO LISTAN

function doLottery(numbers, num) {
  const row = [];
  let r;
  for (let i = 0; i < num; i++) {
    let ok = false;

    while (!ok) {
      ok = true;
      r = Math.floor(Math.random() * numbers) + 1;
      for (let j = 0; j < i + 1; j++) {
        if (row [j] === r) {
          ok = false;
        }
      }
    }
    row[i] = r;
  }
  return row;
}

const lottery = doLottery(40, 7);
for (let i = 0; i < lottery.length; i++) {
  console.log(lottery[i]);
}

//
//
//
// NUOLIFUNKTIOT eli ARROW FUNTIONS

const quadraticSumz = (a, b) => (a * a + b * b);
console.log(quadraticSumz(3, 5));

const quadraticSumsz = (a, b) => {
  console.log('quadraticSum was called.');
  return (a * a + b * b);
};
console.log(quadraticSumsz(3, 5));

//
//
//
//
//
// BOM handling DOM

const secondz = document.getElementsByTagName('li')[1];  // getElementsByTagname returns an array. The indexes in an array start at zero, so 1 means the second <li> element.
const seconds = document.querySelectorAll('li')[1];      // the same with querySelectorAll-function
console.log(secondz);
console.log(seconds);

const bullets = document.querySelectorAll('li');

for (let bullet of bullets) {
  bullet.innerHTML = `<b>${bullet.innerHTML}</b>`;
}

// alternative syntax using array.forEach()
/*
bullets.forEach(function (bullet) {
 bullet.innerHTML = `<b>${bullet.innerHTML}</b>`;
})
*/

