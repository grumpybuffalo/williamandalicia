const weddingDate = new Date("11/8/19");
const MS_IN_DAY = 60 * 60 * 24 * 1000;
let currentCountdown = 298;
let daysRemaining;
const topImg = document.querySelector("#top-img");
let lastUpdateTime;

if (topImg.complete) {
  showCountdown();
} else {
  topImg.addEventListener("load", showCountdown);
}

function showCountdown() {
  document.querySelector("#days-to-go-text").style.opacity = 1;
  computeDaysRemaining();
}

function computeDaysRemaining() {
  var now = new Date();
  daysRemaining = Math.ceil((weddingDate - now) / MS_IN_DAY);
  lastUpdateTime = window.performance.now();
  updateCountdown();
}

function updateCountdown(timestamp) {
  if (currentCountdown > daysRemaining) {
    if (timestamp - lastUpdateTime > 30) {
      currentCountdown--;
      document.querySelector("#countdown").innerHTML = currentCountdown;
      lastUpdateTime = timestamp;
    }
    requestAnimationFrame(updateCountdown);
  } else {
    now = new Date();
    msFromMidnight = now.getHours() * 60 * 60 * 1000 + now.getMinutes() * 60 * 1000 + now.getSeconds() * 1000 + now.getMilliseconds();
    msToMidnight = MS_IN_DAY - msFromMidnight;
    setTimeout(computeDaysRemaining, msToMidnight);
  }
}
