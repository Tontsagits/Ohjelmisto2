'use strict';

// BOM DOM and EVENT HANDLING
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

// getElementsByTagName returns an array.
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
// Select the element in the document with the id 'container'
// and save the element node as 'u'.
// Then select all p-elements from the element node 'u'
// and save the element list as 'p':
const u = document.getElementById('container');
const p = u.getElementsByTagName('p');

// the same can also be written without an intermediate variable
const p1 = document.getElementById('container').getElementsByTagName('p');

// or with a single command using the CSS selector
const p2 = document.querySelectorAll('.container p');

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

//
//
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
// Adding HTML to a document using string:

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

// create img element
const i = document.createElement('img');
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
