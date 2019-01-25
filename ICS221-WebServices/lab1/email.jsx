const React = require('react');

const Email = (props) => {
    return(
        <div>
            <h1>Thank you {(props.name) ? props.name : ""}for signing up</h1>
            <p>If you have and questions, please contact the support.</p>
        </div>
    )
}

module.exports = Email;