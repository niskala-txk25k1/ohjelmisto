"use strict";

document.querySelector("#source").addEventListener("submit", (e)=>{
	e.preventDefault();
	let f = document.querySelectorAll("input");
	document.querySelector("#target").innerText = `Your name is ${f[0].value} ${f[1].value}`
})
