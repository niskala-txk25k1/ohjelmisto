"use strict";

const p = document.querySelector("#trigger");
const img = document.querySelector("#target");

p.addEventListener("mouseover", ()=>{
	img.src = "img/picB.jpg";
});

p.addEventListener("mouseout", ()=>{
	img.src = "img/picA.jpg";
});

