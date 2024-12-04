'use strict';

//
//
//
// Konsoli tulostus

console.log('Hello Javascript World!');

//
//
//
//
//
//
// Muuttuja

let muuttuja;
muuttuja = 'Hank Moody';
console.log(`Hello, ${muuttuja}`);

//
//
//
//
//
//
// Vakio

const vakio = 'Oh, Another Hank Moody';
console.log(vakio);

//
//
//
//
//
//
// alert popup, pysäyttää ohjelman kunnes ok

alert('Alert! Hello JavaScript World!!!');

//
//
//
//
//
//
// Kysytään tietoja promptilla

const name = prompt('Anna nimesi:', 'Nimi tähän.');
console.log((`Inserting to HTML: 'Hello, ${name}!'`));
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
//
//
//
//
//
//
// String vai Numero PARSE ja tulostus

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
//
//
//
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
console.log(`Inserting to HTML: ${greeting}`);
document.querySelector('#testingpara2').innerHTML = greeting;

//
//
//
//
//
//
//
//
//
//  OPERAATTOREITA plus ja miinus
// yhteenlasku, kertolasku, jakolasku

let number = 3;
console.log(`Number is ${number}`);
number = number * 7;     // the value is now 21
console.log(`Now number is ${number}`);
number = 1 + number / 2;   // the value is now 11.5
console.log(`Now number is ${number}`);
console.log(number);

//  operaattoreita
//
//
//
// yhteenlasku, vähennyslasku

number = 3;
console.log(`Now number is ${number}`);
number++;     // the value is now 4
console.log(`Now number is ${number}`);
number--;     // the value is again 3
console.log(`Now number is ${number}`);
console.log(number);

//
// yhteenlasku, vähennyslasku, kertolasku, jakolasku

number = 3;
number *= 2;    // the value is now 6
console.log(`Now number is ${number}`);
number /= 3;    // the value is now 2
console.log(`Now number is ${number}`);
number += 7;   // the value is now 9
console.log(`Now number is ${number}`);
number -= 8;    // the value is now 1
console.log(`Now number is ${number}`);
console.log(number);

//
//
//
//
//
//
//
//
//
// Matematiikka objekti Math

console.log('Using Math Object to do some math....');
console.log(`Squareroot of 3 is...`);
console.log(Math.sqrt(3));
console.log(`Tässä numeron 3 neliöjuuri: ${Math.sqrt(3)}`);
console.log(`Some random numbers between 0 and 1...`);
console.log(Math.random());
console.log(Math.random());
console.log(Math.random());
console.log(Math.random());
console.log(Math.random());
console.log(Math.random());

//
//
//
//
//
//
//
//
//
// määrätyt vakiot Designated Constants

const multiplier = 4.1868;
console.log(`Multiplier number is ${multiplier}`);
const k1 = prompt('Give the amount of energy for lunch (kcal).');
const k2 = prompt('Enter the amount of energy for dinner(kcal).');

const j1 = multiplier * k1; // näköjään hyväksyy stringin sisällön kertoimeen
const j2 = multiplier * k2;

console.log(`At breakfast you got ${j1} kJ and at dinner you got ${j2} kJ.`);

//
//
//
//
//
//
//
//
//
// WHILE loop, tarkastus aina iteraatiota ENNEN eli ALUSSA while rivillä

let weight = prompt('Enter weight (kg) (must be positive).');
while (weight <= 0) {
  weight = prompt('The weight must be positive. Re-enter the weight (kg).');
}
console.log('You entered the weight: ' + weight + ' kg.');

//
//
//
// DO WHILE loops, TARKASTUS LOPUSSA eli WHILE rivillä

let result;
do {
  result = Math.floor(Math.random() * 6) + 1;
  console.log('some random numbers between 1 and 6...');
  console.log(result);
} while (result < 6);

//
//
//
// FOR loops

console.log('Numbers from 1 to 10...');
for (let i = 1; i <= 10; i++) {
  console.log(i);
}

//
//
//
// Nested FOR loops

console.log('Some multiplication from 1 to 5...');
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
//
//
//
//
//
//
//
//
//
// LIST ARRAYS

console.log('ARRAYS aka LISTS!');

let numbers = []; // vakio, mutatoituva
numbers = [17, 2, 8];

for (let i = 0; i < numbers.length; i++) {
  console.log(`Array item: ${numbers[i]}`);
}

const names = ['Frank', 'Scott', 'Jasmine', 'Don'];

for (let i = 0; i < names.length; i++) {
  console.log(`Names: ${names[i]}`);
}

for (let name of names) {
  console.log(`Names again: ${name}`);
}

//
//
//
//
//
//
//
//
//
//
//
//
// OBJECT LITERALS (like Python dictionary)

console.log('This is OBJECT LITERAL! aka a dictionary of sorts...');

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

console.log('Adding address to student...');
student.address = 'Schoolroad 7';  // adds 'address' property to previous example
console.log('And removing phone number...');
delete student.phone;              // deletes 'phone' property from previous example

console.log('Updated student infos...');
console.log(student);

const chosenProperty = 'lastName';
console.log(student[chosenProperty]);
console.log(`Students lastname is: ${student[chosenProperty]}`);

//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
// FUNKTIOT ilman paluuarvoa

console.log('FUNCTIONS!');

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
//
//
//
// FUNKTIOT paluuarvoilla

console.log('Quadratic Sum function as example...');

function quadraticSum(first, second) {
  const result = first * first + second * second;
  return result;
}

const num1 = prompt('Enter 1. number.');
const num2 = prompt('Enter 2. number.');
console.log('Calling quadraticSum function...');
const quad = quadraticSum(num1, num2);
console.log('The quadratic sum of ' + num1 + ' and ' + num2 + ' is ' + quad);

//
//
//
//
//
//
//
//
//
//
//
//
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
//
//
//
//
//
//
//
//
//
//
//
//
// ARRAY as PARAMETER of a FUNCTION

console.log('ARRAYS aka LISTS again now as FUNCTION PARAMETER!');

function grow(array) {
  for (let i = 0; i < array.length; i++) {
    array[i]++;
  }
  return;
}

const numberz = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21];

console.log('Calling function numberz...');
grow(numberz);

// tulostetaan eka ja toka ja kolmas alkio arrayssa
console.log('Printing to console: 1st, 2nd and 3rd alkio for array...');
console.log(numberz[0] + ' ' + numberz[1] + ' ' + numberz[2]);

// tulostetaan KAIKKI alkiot listalta
console.log('Printing to console all members of the array...');
for (let i = 0; i < numberz.length; i++) {
  console.log(`Listalla on luku: ${numberz[i]}`);
}

//
//
//
//
//
//
//
//
//
// LOTTO ARVONTA FUNKTIO JOKA LUO LISTAN

console.log('Creating some funky lottery numbers for ya all.......');

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
console.log('Did you win?');

//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
// NUOLIFUNKTIOT eli ARROW FUNTIONS

console.log('ARROW FUNCTIONS!');

console.log('quadSumz using ArrowFunction...');
const quadraticSumz = (a, b) => (a * a + b * b);
console.log(quadraticSumz(3, 5));

console.log('Another quadSumsz using ArrowFunction structure...');
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
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
// BOM handling DOM

console.log('Now we do some BOM and DOM stuff. Nice!');

//
//
//
// Select the 2nd item (i.e. <li>) in the list <ul>:

// getElementsByTagname returns an array.
// The indexes in an array start at zero, so 1 means the second <li> element.
const secondz = document.getElementsByTagName('li')[1];
// the same with querySelectorAll-function
const seconds = document.querySelectorAll('li')[1];

console.log('Here are some HTMl LI elements from the document...');
console.log(secondz);
console.log(seconds);

//
//
//
//
//
// select all LI elements
console.log('Loading all LI elements from HTML document and making them BOLD.');
const bullets = document.querySelectorAll('li');

// Iterate all <li> elements using the forEach function and make the text bold.
// ADD <b> tags into HTML
for (let bullet of bullets) {
  bullet.innerHTML = `<b>${bullet.innerHTML}</b>`;
}

// alternative syntax using array.forEach()
/*
bullets.forEach(function (bullet) {
 bullet.innerHTML = `<b>${bullet.innerHTML}</b>`;
})
*/

//
//
//
//
//
//
//
//
// Select the element in the document with the id 'news' 'container' and save the element node as 'u'.
// Then select all p-elements from the element node 'u' and save the element list as 'p':
const u = document.getElementById('container');
const p = u.getElementsByTagName('p');

// the same can also be written without an intermediate variable
const p1 = document.getElementById('container').getElementsByTagName('p');

// or with a single command using the CSS selector
const p2 = document.querySelectorAll('#container p');

console.log('Here are some HTML elements from the HTML document. Enjoy!');
console.log(u); // whole DIV id container
console.log(p); // HTML collection
console.log(p1); // HTML collection
console.log(p2); // Node list

//
//
//
//
//
//
// Change the content of an HTML element:

console.log('Setting blue Monday to red Tuesday inside HTML....');
document.getElementById('date').innerHTML = '<span class="red">Tuesday</span>';

//
//
//
//
//
//
// Change the value of an attribute in HTML element:

console.log(
    'Changing the Metropolia logo to Laurea logo inside HTML document... Cool!');
// the attribute name is used as the property
document.getElementById('logo').src = 'laurealogo.png';
// or setAttribute() function for older browsers
document.getElementById('logo').setAttribute('src', 'laurealogo.png');

//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
// Adding HTML to a document:

console.log(
    'Add some text and a picture of a cat into HTML document to a DIV...');

// get element whose id is 'example'
const div = document.querySelector('#example');
// to make a multiline string, note the backtick around the string
const html =
    `<p>Here is some of text with a picture.</p>
     <p><img src="https://placecats.com/300/200" alt="Cat" title="Picture of a cat."/></p>`;
div.innerHTML = html; // sets the string 'html' to the HTML content of the selected element

//
//
// Same with DOM functions

console.log(
    'Add some text and a picture of a cat into HTML document to another DIV...');

// get element whose id is 'example2'
const div2 = document.querySelector('#example2');

const i = document.createElement('img');  // create img element
i.src = 'https://placecats.com/300/200';    // set src attribute
i.alt = 'Cat';                            // set alt attribute
i.title = 'Picture of a cat.';          // set title attribute

// create text node
const t = document.createTextNode('Here is some of text with a picture.');

// create p element
const p5 = document.createElement('p');
p5.appendChild(t);     // add text to p element
// create another p element
const p6 = document.createElement('p');
p6.appendChild(i);     // add image to p element

div2.appendChild(p5);   // add p element to the selected element from the HTML document
div2.appendChild(p6);   // add p element to the selected element from the HTML document
// at this point new HTML will appear in the document.

//
//
//
//
//
//
//
//
//
//
//
// EVENT HANDLING

const button = document.querySelector('button');
button.addEventListener('click', function(evt) {
      alert('Element ' + evt.currentTarget.tagName + ' was clicked');
    },
);

// VOI OLLA MYÖS VIITTAUS FUNKTIOON
/*
const button = document.querySelector('button');

function popup(evt){
  alert('Element ' + evt.currentTarget.tagName + ' was clicked');
}

button.addEventListener('click', popup);
 */

const nappi = document.querySelector('button');

function A(evt) {
  alert('This is function A');
  nappi.removeEventListener('click', A);
  nappi.addEventListener('click', B);
}

function B(evt) {
  alert('This is function B');
}

nappi.addEventListener('click', A);

//
//
//
//
// FORM EVENTS
//

// select the elements
const form = document.querySelector('form');
const fName = document.querySelector('input[name=fName]');
const lName = document.querySelector('input[name=lName]');
const p7 = document.getElementById('match');

// When the form is submitted...
form.addEventListener('submit', function(evt) {
  // ... prevent the default action.
  evt.preventDefault();
  // Here you can check, for example, whether the fields on the form have been filled in correctly,
  // after which it could be sent using the fetch method, for example
  // However, for now, let's print the user input as an example.
  p7.innerText = `Your name is ${fName.value} ${lName.value}`;
});

//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
// AJAX
// Asynchronous data transfer
//

console.log('the script starts');

function synchronousFunction() {
  let number = 1;
  for (let i = 1; i < 100000; i++) {
    number += i;
    console.log('synchronousFunction running');
  }
  console.log('regular function complete', number);
}

// asynchronous function is defined by the async keyword
async function asynchronousFunction() {
  console.log('asynchronous download begins');
  try {                    // error handling: try/catch/finally
// starting data download, fetch returns a promise which contains an object of type 'response'
    const response = await fetch('http://127.0.0.1:3000/airport/00A');
// modify the data retrieved from the response object using the json() function
    const jsonData = await response.json();
    console.log(jsonData.ICAO, jsonData.Name);    // log the result to the console
  } catch (error) {
    console.log(error.message);
// finally = this is executed anyway, whether the execution was successful or not
  } finally {
    console.log('asynchronous load complete');
  }
}

synchronousFunction();
asynchronousFunction();

console.log('the script ends');
