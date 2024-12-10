'use strict';

let outPutStr = 'Nice...';

const butTE = document.querySelector('input[type="submit"]');
const formTE = document.querySelector('#source');
const pTE = document.querySelector('#target');

butTE.addEventListener('click', function(evt) {
  evt.preventDefault();
  const firstName = formTE.querySelector('input[name="firstname"]').value;
  const lastName = formTE.querySelector('input[name="lastname"]').value;
  console.log(firstName);
  console.log(lastName);
  outPutStr = firstName + ' ' + lastName;
  pTE.innerHTML = `${outPutStr}`;
});
