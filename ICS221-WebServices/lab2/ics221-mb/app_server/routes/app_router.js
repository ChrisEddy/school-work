const express = require('express');
const router = express.Router();
const msgController = require('../controllers/msg');


// get home page
router.get('/', msgController.index);

module.exports = router;