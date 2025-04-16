'use strict';
const names = ['John', 'Paul', 'Jones'];

const ul = document.querySelector("#target");

for (const label of names) {
	//const li = document.createElement("li");
	//li.innerText = `${label}`;
	//ul.appendChild(li);
	ul.innerHTML += `<li>${label}</li>`;
}

