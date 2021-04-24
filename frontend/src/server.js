const cors = require('cors');
const express = require('express');
const helmet = require('helmet');
const morgan = require('morgan');

const server = express();

server.use(cors());
server.use(helmet());
server.use(morgan('dev'));
server.use(express.json());
server.use(express.urlencoded({ extended: true }));
server.use(express.static('public'));
server.use(function(req, res, next) {
  res.setHeader("Content-Security-Policy", "connect-src 'self' localhost:* ws://localhost:*;");
  return next();
});

server.listen(80, err => {
  if (err) {
    console.error(err);
  }
});
