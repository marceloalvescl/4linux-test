const usernameTextInput = document.getElementById('username');
const passwordTextInput = document.getElementById('password');

const loginBtn = document.getElementById('loginBtn');

loginBtn.addEventListener('click', onLogin);

function onLogin(event) {
  event.preventDefault();

  const username = usernameTextInput.value;
  const password = passwordTextInput.value;

  const body = JSON.stringify({ username, password });

  console.log(`Sending = ${body}`);

  fetch('http://127.0.0.1:81/login', {
    method: 'POST',
    body: body
  })
    .then(response => response.json())
    .then(json => console.log(`Received = ${json}`))
    .catch(err => console.error(err));
}
