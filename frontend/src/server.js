const express = require('express');
const path = require('path');
const fetch = require('node-fetch');
/**
 * Rotas do front.
 */

const server = express();
server.set('view engine', 'ejs');
server.use(express.json());
server.use(express.urlencoded({ extended: true }));
server.use(express.static(path.join(__dirname, '..', '/public')));

server.get('/', function(request, response){
  fetch('http://127.0.0.1:81/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', "Cookie": request.get("Cookie") },
  }).then(async (res) => {  
    return [await res.json(), res.status];
  })
  .then(([jsonData, status]) => {
    console.log(jsonData);
    console.log(status);
    response.render(path.join(__dirname, '..', 'public', 'home.ejs'), {json: jsonData});
  })
  .catch((err) => {
    response.redirect('/login');
  });
})

server.get('/login', function(request, response){
  response.sendFile(path.join(__dirname, '..', 'public', 'login.html'));
})

server.post('/process-login', function(request, response){
  let body = {
    username: request.body['username'],
    password: request.body['password']
  }
  let apiResponse;
  fetch('http://127.0.0.1:81/login', {
    method: 'POST',
    body: JSON.stringify(body),
    headers: { 'Content-Type': 'application/json' },
  }).then(res => {
    apiResponse = res.status;
    setCookieHeader = res.headers.get('Set-Cookie')
    return res.json();
  }).then(json => {
    console.log(json);
    if(apiResponse == 201){
      console.log(setCookieHeader)
      response.setHeader('Set-Cookie', setCookieHeader)
      response.redirect(301, '/');
    }else{
      response.redirect('/login');
    }
  })
})

server.post("/logoff", function(request, response, next) {
  fetch('http://127.0.0.1:81/logout', {
    method: 'POST',
  }).then(res => {
    apiResponse = res.status;
    setCookieHeader = res.headers.get('Set-Cookie')
    return res.json();
  }).then(json => {
    console.log(json);
    if(apiResponse == 201){
      console.log(setCookieHeader)
      response.setHeader('Set-Cookie', setCookieHeader)
      response.redirect(301, '/');
    }else{
      response.redirect('/login');
    }
  })
  response.clearCookie('session');
  response.redirect('/login');
});

server.listen(80, err => {
  if (err) {
    console.error(err);
  }
});
