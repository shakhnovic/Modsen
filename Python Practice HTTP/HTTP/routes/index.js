var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
  res.render('index', { title: 'Weather API' });
});

router.post('/', function(req, res, next) {
  res.json({ message: 'POST request received' });
});

router.patch('/', function(req, res, next) {
  res.json({ message: 'PATCH request received' });
});

router.put('/', function(req, res, next) {
  res.json({ message: 'PUT request received' });
});

router.delete('/', function(req, res, next) {
  res.json({ message: 'DELETE request received' });
});

router.get('/hello', (req, res) => {
  res.send('Hello World!');
});

module.exports = router;
