const React = require('react');
const MsgList = require('../components/msgList');

const MsgBoard = (props) => {
    super(props);
    this.state = {
        messages: this.props.messages,
    };
    
    return(
        <div className="MsgBoard">
            <MsgList messages={this.state.messages}/>
        </div>
    )
}

module.exports = MsgBoard;