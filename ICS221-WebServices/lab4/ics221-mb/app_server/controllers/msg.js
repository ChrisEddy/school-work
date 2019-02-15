'use strict';

const React = require('react');
const ReactDOMServer = require('react-dom/server'); 

require('es6-promise').polyfill();
require('isomorphic-fetch');
require("@babel/register") ({presets: [ '@babel/preset-react' ]});

const Header = React.createFactory(require('../components/Header.jsx'));
const Footer = React.createFactory(require('../components/Footer.jsx'));
const MsgBoard = React.createFactory(require('../components/MsgBoard.jsx'));

function handleHTTPErrors(response){
    if(!response.ok) throw Error(response.status +
    ': ' + response.statusText);
    return response;
}

const getMessages = (req, res) => {
    fetch('http://localhost:3003/msgs')
    .then(response=> handleHTTPErrors(response))
    .then(result=> result.json())
    .then(result=> {
      if (!(result instanceof Array)) {
        console.error('API lookup error');
        result = [];
      } else {
        renderIndex(req, res, result);
      }
    })
    .catch(error=> {
      console.log(error);
    });
  }

// const msgs = [
//     { id: 0, name: 'Bill', msg: 'Hi All!' },
//     { id: 1, name: 'Ann', msg: 'ICS 221 is fun!' },
//     { id: 2, name: 'John', msg: 'Howdy!' },
//     { id: 3, name: 'Barb', msg: 'Hi'},
//     { id: 4, name: 'Frank', msg: 'Who\'s tired?'},
//     { id: 5, name: 'Sarah', msg: 'I heart React' }
// ];

// index handler
const renderIndex = (req, res, msgs) => {
    res.render('index', {
        title: 'ICS 221 Universal JS Msg Board',
        header: ReactDOMServer.renderToString(Header()),
        footer: ReactDOMServer.renderToString(Footer()),
        msgBoard: ReactDOMServer.renderToString(MsgBoard(   {   messages: msgs  }   )),
        props: '<script>let messages=' + JSON.stringify(msgs.reverse()) + '</script>'
    });
};

module.exports = { getMessages };