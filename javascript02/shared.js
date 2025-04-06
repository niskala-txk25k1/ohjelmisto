"use strict";

function promptInt(text)
{
	return parseInt( prompt(text) );
}

function promptFloat(text)
{
	return parseInt( prompt(text) );
}


function put_li(text)
{
	const output = document.querySelector("#output");
	const li = document.createElement("li");
	li.innerHTML = text;
	output.append(li);
}

function put(text)
{
	const output = document.querySelector("#output");
	output.innerHTML += text;

}
