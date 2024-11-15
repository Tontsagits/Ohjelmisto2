'use strict';

const koirat = [];

for (let i = 0; i < 5; i++) {
  koirat.push(prompt(`Kirjoita koiran ${i + 1}. nimi:`));
}

koirat.sort((a, b) => a - b);
koirat.reverse();

// console.log(koirat);

for (let koira of koirat) {
  const koodi = `<li>${koira}</li>`;
  document.querySelector('#kohde').innerHTML += koodi;
}
