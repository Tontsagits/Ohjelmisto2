'use strict';

const numOfParticipants = parseInt(
    prompt('Montako osallistujaa?', 'Osallistujien määrä tähän.'));

// alustetaan lista
const names = [];

// lisätään nimet listaan
for (let i = 1; i <= numOfParticipants; i++) {
  let name = '';
  name = prompt('Anna osallistujan nimi:', 'Osallistujan nimi tähän.');
  names.push(name);
}

// järjestetään lista aakkosjärjestykseen
names.sort();

// luodaan apumuuttuja
let namesStr = ``;

// jokaista nimeä kohti lisätään nimi tekstikenttään LI tagien kanssa
for (let name of names) {
  console.log(name);
  namesStr += `<li>${name}</li>`;
}
// lisätään syntynyt teksti HTML koodiin
document.querySelector('#tag1').innerHTML = `${namesStr}`;
