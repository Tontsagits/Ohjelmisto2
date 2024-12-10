'use strict';

const pTE = document.querySelector('#trigger');
const imgTE = document.querySelector('#target');

pTE.addEventListener('mouseover', function(evt) {
  imgTE.src = 'img/picB.jpg';
});
pTE.addEventListener('mouseout', function(evt) {
  imgTE.src = 'img/picA.jpg';
});
