'use strict';

// alustetaan lista koirista
const koirat = [];

// kysytään kuuden koiran nimet
for (let i = 0; i < 5; i++) {
  koirat.push(prompt(`Kirjoita ${i + 1}. koiran nimi:`, 'Koiran nimi tähän.'));
}

// järjestetään koirat aakkosjärjestykseen
koirat.sort();
// vaihdetaan järjestys päinvastoin
koirat.reverse();

// jokaista koiraa kohden
for (let koira of koirat) {
  // luodaan muuttuja jossa HTML tagit ja tekstisisältö
  const koodi = `<li>${koira}</li>`;
  // lähetetään syntynyt muuttuja valitun HTML tagin sisällöksi
  document.querySelector('#tag1').innerHTML += koodi;
}
