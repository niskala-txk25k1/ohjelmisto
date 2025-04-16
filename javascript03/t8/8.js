"use strict";

const start = document.querySelector("#start");
const op = document.querySelector("#operation");
const num1 = document.querySelector("#num1");
const num2 = document.querySelector("#num2");
const result = document.querySelector("#result");

start.addEventListener("click", ()=>{

	const a = parseInt(num1.value);
	const b = parseInt(num2.value);
	let res = 0;

	switch (op.value) {
	case "add":
		res = a + b;
		break;
	case "sub":
		res = a - b;
		break;
	case "multi":
		res = a * b;
		break;
	case "div":
		res = a / b;
		break;
	}

	result.innerText = res;
});
