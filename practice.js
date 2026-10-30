let name = "Alice";
let age = 20;
console.log(`My name is ${name} and I am ${age} years old.`);

function greet(name) {
    return `Hello, ${name}!`;
}
console.log(greet("Alice")); // should return "Hello, Alice!"

const numbers = [2, 82, 1, 3, 6];
const evens = numbers.filter(function(num) {
    return num % 2 === 0;
});
console.log(evens);

function validateEmail(email) {
    return email.includes("@") && email.includes(".");
}

const button = document.querySelector('#myButton');

button.addEventListener('click', () => {
  document.querySelector('h1').style.color = 'blue';
});
const navToggle = document.querySelector('#navToggle');
const navLinks = document.querySelector('#navLinks');

navToggle.addEventListener('click', () => {
  navLinks.classList.toggle('hidden');
});
const darkModeToggle = document.querySelector('#darkModeToggle');

darkModeToggle.addEventListener('click', () => {
  document.body.classList.toggle('dark');
});
const form = document.querySelector('#myForm');
const emailInput = document.querySelector('#emailInput');
const formError = document.querySelector('#formError');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  if (!validateEmail(emailInput.value)) {
    formError.textContent = 'Please enter a valid email.';
    formError.classList.remove('hidden');
  } else {
    formError.classList.add('hidden');
    console.log('Form submitted successfully!');
  }
});