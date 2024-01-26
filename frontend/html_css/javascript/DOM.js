////////////////////////////////////////////////////////////////
// DOM
const container = document.querySelector('#container');

const content = document.createElement('div');
content.classList.add('content');
content.textContent = 'This is the glorious text-content!';

container.appendChild(content);

const p1 = document.createElement('p');
p1.style.color = 'red';
p1.textContent = 'Hey I’m red!'
container.appendChild(p1);

const h3 = document.createElement('h3');
h3.style.color = 'blue';
h3.textContent = 'Hey I’m blue h3!'
container.appendChild(h3);

////////////////////////////////////////////////////////////////
const div = document.createElement('div');
div.style.cssText = 'border-style: solid; border-color: black; background-color: pink;'

const h1 = document.createElement('h1');
h1.textContent = 'I’m in a div'
div.appendChild(h1);

const p2 = document.createElement('p');
p2.textContent = 'ME TOO!'
div.appendChild(p2);

container.appendChild(div);

////////////////////////////////////////////////////////////////
// Events
const btn = document.querySelector('#btn');
btn.onclick = () => alert("Hello World");

const btn2 = document.querySelector('#btn2');
btn2.addEventListener('click', () => {
  alert("Hello World");
});

const btn3 = document.querySelector('#btn3');
btn3.addEventListener('click', function (e) {
  e.target.style.background = 'blue';
})

////////////////////////////////////////////////////////////////
// ForEach
const buttons = document.querySelectorAll('button');

// we use the .forEach method to iterate through each button
buttons.forEach((button) => {

  // and for each one we add a 'click' listener
  button.addEventListener('click', () => {
    alert(button.id);
  });
});
