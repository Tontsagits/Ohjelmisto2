'use strict';

// määritellään vakiot

const lomake = document.querySelector('form');
const hakusana = document.querySelector('input');
const tiedot = document.querySelector('#tiedot');

// kartta näkyviin

const map = L.map('map').setView([60.2, 24.6], 8);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

lomake.addEventListener('submit', function(evt) {
  evt.preventDefault();
  const kaupunki = hakusana.value;
  fetchWeather(kaupunki);
});

// HakuLomake

const APIKey = '8891ed0ba67dbb011bea8d0213972a42';

// const kaupunki = 'Forssa';

// const request = `https://api.openweathermap.org/data/2.5/weather?units=metric&appid=${APIKey}&q=${kaupunki}`;

async function fetchWeather(kaupunki) {
  const request = `https://api.openweathermap.org/data/2.5/weather?units=metric&appid=${APIKey}&q=${kaupunki}`;

  try {
    const response = await fetch(request);
    if (!response.ok) {
      throw new Error('Server not found');
    }

    const weather = await response.json();
    // const name = weather.name;
    // const temp = weather.main.temp;
    // console.log(weather);
    // console.log(`Name: ${name}`);
    // console.log(`Temperature: ${temp}C`);

    // otsikko
    const otsikko = document.createElement('h3');
    otsikko.innerText = weather.name;

    // lampotila
    const lampo = document.createElement('p');
    lampo.innerText = `Lämpötila: ${weather.main.temp}C`;

    // tuulen nopeus ja suunta

    const kaikkiTiedot = document.createElement('article');
    kaikkiTiedot.append(otsikko, lampo);
    tiedot.innerHTML = '';
    tiedot.appendChild(kaikkiTiedot);

    // Keskitä kartta
    map.setView([weather.coord.lat, weather.coord.lon], 8);

    // Layer
    const marker = L.marker([weather.coord.lat, weather.coord.lon]).addTo(map);

  } catch (error) {
    console.log(error.message);
  }
};

// fetchWeather();
