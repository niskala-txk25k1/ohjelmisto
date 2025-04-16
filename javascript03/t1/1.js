"use strict";

const ul = document.querySelector("#target");

["First", "Second", "Third"].forEach(label=>{
	ul.innerHTML += `<li>${label} item</li>`;
});

