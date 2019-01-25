const ReactDOMServer = require('react-dom/server');
const React = require('react');
require("@babel/register") ({
    presets: ['@babel/preset-react']
});
const email = React.createFactory(require('./email.jsx'));

const emailString = ReactDOMServer.renderToString(email());
console.log(emailString);

const emailStringWithName = ReactDOMServer.renderToString(
    email({name: 'Johnny Castaway'})
)
console.log(emailStringWithName)
