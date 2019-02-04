const express = require('express');
const router = express.Router();
const mainController = require('../controllers/main');

/* GET home page. */
router.get('/', mainController.index);
/* GET about page. */ 
router.get('/about', mainController.about)

module.exports = router;