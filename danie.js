const noButton = document.getElementById("no");
const yesButton = document.getElementById("yes");
const askCard = document.getElementById("ask");
const thanksCard = document.getElementById("thanks");
const message = document.getElementById("message");
const copyButton = document.getElementById("copy");
const accountNumber = document.getElementById("account-number");

const lines = [
  "Hmm, the No button seems to be broken.",
  "Try again. It's really committed to running away.",
  "Think of the snacks.",
  "I'll pay you back. (I won't.)",
  "The Yes button is looking bigger, huh?",
  "Just tap Yes. It's right there."
];

let dodges = 0;

function dodge(event) {
  event.preventDefault();

  const x = Math.random() * (window.innerWidth - noButton.offsetWidth);
  const y = Math.random() * (window.innerHeight - noButton.offsetHeight);

  noButton.style.position = "fixed";
  noButton.style.left = x + "px";
  noButton.style.top = y + "px";

  message.textContent = lines[Math.min(dodges, lines.length - 1)];
  dodges = dodges + 1;

  const size = Math.min(1 + dodges * 0.15, 2);
  yesButton.style.transform = "scale(" + size + ")";
}

noButton.addEventListener("mouseover", dodge);
noButton.addEventListener("touchstart", dodge, { passive: false });
noButton.addEventListener("click", dodge);

yesButton.addEventListener("click", function () {
  askCard.classList.add("hidden");
  thanksCard.classList.remove("hidden");
});

copyButton.addEventListener("click", function () {
  navigator.clipboard.writeText(accountNumber.textContent);
  copyButton.textContent = "Copied!";
});