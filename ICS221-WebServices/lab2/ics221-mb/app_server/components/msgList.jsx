const React = require('react');

const MsgList = (props) => {
    return(
        <div className="MsgList">
            <table className="table table-striped table-bordered">
                <tr>
                    <th className="w-25"></th>
                    <th className="w-25"></th>
                    <th className="w-50"></th>
                </tr>
                <tbody>
                {props.messages.sort((a, b) => a.id - b.id).
                reverse().map( (message, index) =>
                <tr key={message.id}>
                    <td>{index+1}</td>
                    <td>{message.name}</td>
                    <td>{message.msg}</td>
                </tr>
                )}
                </tbody>
            </table>
        </div>
    )
}

module.exports = MsgList;