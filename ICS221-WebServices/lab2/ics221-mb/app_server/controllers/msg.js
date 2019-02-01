'use strict';
const React = require('react');
const ReactDOMServer = require('react-dom/server');

const Header = require('../components/header.jsx');
const Footer = require('../components/footer.jsx');
const MsgBoard = require('../components/msgBoard.jsx');

require("@babel/register")({presets: [ '@babel/preset-react' ]});

React.createFactory(Header);
React.createFactory(Footer);
React.createFactory(MsgBoard);

// temp hard-coded data
const msgs = [
    { id: 1, name: 'Bill', msg: 'Hi All!' },
    { id: 2, name: 'Ann', msg: 'ICS 221 is fun!' },
    { id: 3, name: 'John', msg: 'Howdy!' },
    { id: 4, name: 'Barb', msg: 'Hi' },
    { id: 5, name: 'Frank', msg: 'Who\'s tired?' },
    { id: 6, name: 'Sarah', msg: 'I heart React' }
];

// index handler
const index = (req, res) => {
    res.render('index', {
      title: 'ICS 221 Universal JS Msg Board',
      header: ReactDOMServer.renderToString(Header()),
      footer: ReactDOMServer.renderToString(Footer()),
      msgBoard: ReactDOMServer.renderToString(MsgBoard(
        { messages: msgs }
      )),
      props: '<script>let messages=' + JSON.stringify(msgs.reverse()) +
       '</script>'
    });
};

module.exports = { index };
