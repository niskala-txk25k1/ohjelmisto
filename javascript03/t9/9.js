const start = document.querySelector("#start");
const input = document.querySelector("#calculation");
const result = document.querySelector("#result");

// >You can use the includes and split methods.
// I decided not to use them :) 

start.addEventListener("click", ()=>{

	let op = '';
	let i = 0;
	let n = [0, 0];

	for (let c of input.value) {
		const code = c.charCodeAt(0);
		if (code >= 48 && code <= 57) {
			n[i] *= 10;
			n[i] += code - 48;
		} else {
			op += c;
			i=1;
		}
	}

	switch (op) {
	case "+":
		result.innerText = n[0] + n[1];
		break;

	case "-":
		result.innerText = n[0] - n[1];
		break;

	case "/":
		result.innerText = n[0] / n[1];
		break;

	case "*":
		result.innerText = n[0] * n[1];
		break;

	default:
		result.innerText = "Invalid op";
		break;
	}

})
