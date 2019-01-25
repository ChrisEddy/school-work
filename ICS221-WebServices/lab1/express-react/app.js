// 1. module imports
const express = require('express');
const path = require('path');
const http =  require('http');
const appRouter = require('./app_server/routes/app_router');

const app = express();

// 2. Configuration - Use Pug as our HTML Template Engine
app.set('views', path.join(__dirname, 'app_server', 'views')); app.set('view engine', 'pug');

// 3, Middleware
app.use(express.static(path.join(__dirname, 'public')))

app.use('/', appRouter);

app.use(function(req, res) { 
    res.status(404); 
    res.send('File not found!');
});

http.createServer(app).listen(3000, function() {
    console.log('React Express App started on Port 3000.');
});
