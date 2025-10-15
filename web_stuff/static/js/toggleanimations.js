const buttonsDiv = document.querySelector(".buttons");

const blurbifybutton = buttonsDiv.querySelector("#blurbifybutton");
const Backgroundbutton = buttonsDiv.querySelector("#Backgroundbutton");
const flyingbutton = buttonsDiv.querySelector("#flyingbutton");
const spinbutton = buttonsDiv.querySelector("#spin");

const blurbifydiv = document.querySelector(".blurbifydiv");
const pfpid = document.querySelector("#pfpid");

const body = document.querySelector("body");

const flyingimage = document.querySelector("img.flyingimage");

// now the toggling logic here

Backgroundbutton.addEventListener("click", () => {
  console.log("toggling background");
  body.classList.toggle("background_class");
});

flyingbutton.addEventListener("click", () => {
  console.log("toggling flying object");
  flyingimage.classList.toggle("flying_class");
});

spinbutton.addEventListener("click", () => {
  console.log("toggling spin");
  blurbifydiv.classList.toggle("spin_class");
});
function easeOutQuad(t) {
  return t * (2 - t);
}

function countUp(element, target, duration = 2000) {
  const start = 0;
  const range = target - start;
  const startTime = performance.now();

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const eased = easeOutQuad(progress);
    const value = Math.floor(start + range * eased);

    element.textContent = value.toLocaleString();

    if (progress < 1) {
      requestAnimationFrame(update);
    }
  }

  requestAnimationFrame(update);
}

const views = document.querySelector("#count");
const viewcount = parseInt(views.textContent.replace(/,/g, ""));

// starting up the animation will do a viewcount animation
// add "yes this is what I do instead of sleeping..."
blurbifybutton.addEventListener("click", () => {
  setTimeout(() => {
    console.log("toggling blurbify");
    blurbifydiv.classList.toggle("blurbify_class");
    pfpid.classList.toggle("spin_class");
    countUp(views, viewcount, 5000);
  }, 2000); // 2000ms = 2 seconds
});
