"use strict";

const ul = document.querySelector("#target");

["First", "Second", "Third"].forEach(label=>{
	const li = document.createElement("li");
	li.innerText = `${label} item`;
	ul.appendChild(li);
});

