const React = require('react');
const MsgList = require('./MsgList.jsx');
const NewMsg = require('./NewMsg.jsx');

class MsgBoard extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            messages: this.props.messages
        };
        this.addMessage = this.addMessage.bind(this);
        this.handleHTTPErrors = this.handleHTTPErrors.bind(this);
    }

    componentDidMount(){
        console.log('hello')
        fetch('http://localhost:3003/msgs', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(function(data) {
            console.log(data);
        })
        .catch(function(e) {
            console.log(e);
        });
    }

    

    addMessage(message) {
        console.log('sdbhlgf')
        let msgs = this.state.messages;
     
        // add id attribute
        message.id = msgs.length;
        // append to array
        msgs.push(message);
        // update state var
        this.setState({
          messages: msgs
        });
     
        // update back-end data
        fetch('http://localhost:3003/msgs', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(message)
        })
        .then(response=> this.handleHTTPErrors(response))
        .catch(error=> {
          console.log(error);
        });
    }

    render() {
        return (
            <div>
                <NewMsg addMsgCallback={this.addMessage}/>
                <MsgList messages={this.state.messages}/>
            </div>
        )
    }
}

module.exports = MsgBoard;