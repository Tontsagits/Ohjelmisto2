'use strict';

const u = document.getElementById('target');

const l1 = document.createElement('li');
const t1 = document.createTextNode('First Item');
l1.appendChild(t1);
u.appendChild(l1);

const l2 = document.createElement('li');
const t2 = document.createTextNode('Second Item');
l2.appendChild(t2);
l2.classList.add('my-item');
u.appendChild(l2);

const l3 = document.createElement('li');
const t3 = document.createTextNode('Third Item');
l3.appendChild(t3);
u.appendChild(l3);
