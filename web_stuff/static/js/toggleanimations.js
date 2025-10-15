const buttonsDiv = document.querySelector(".buttons");

const blurbifybutton = buttonsDiv.querySelector("#blurbifybutton");
const Backgroundbutton = buttonsDiv.querySelector("#Backgroundbutton");
const flyingbutton = buttonsDiv.querySelector("#flyingbutton");

const blurbifydiv = document.querySelector(".blurbifydiv");

const body = document.querySelector("body");

const flyingimage = document.querySelector("img.flyingimage");

// now the toggling logic here
blurbifybutton.addEventListener("click", () => {
  console.log("toggling blurbify");
  blurbifydiv.classList.toggle("blurbifyanimations");
});

Backgroundbutton.addEventListener("click", () => {
  console.log("toggling background");
  body.classList.toggle("backgroundanimations");
});

flyingbutton.addEventListener("click", () => {
  console.log("toggling flying object");
  flyingimage.classList.toggle("flyinganimations");
});
