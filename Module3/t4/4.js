'use strict';

// Tämä koodi oli jo valmiina?

const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

// Tämä esimerkki ilman createElement metodia
// Käyttäen innerHTML metodia jolla syötetään koodia
/*
const select = document.querySelector('#target');
for (const student of students) {
  const html = `<option value="${student.id}">${student.name}</option>>`;
  select.innerHTML += html;
}
*/

// Tämä taas createElement metodilla
const select = document.querySelector('#target');
for (const student of students) {
  const option = document.createElement('option');
  option.value = student.id;
  option.innerText = student.name;
  select.appendChild(option);
}
