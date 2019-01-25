const React = require('react');

const About = (props) => {
    return(
        <div>
            <h1>This is a 
                <a href={props.links[0]}>React</a> 
                Component generated  on the server and delivered via
                <a href={props.links[1]}>Node.js</a>
                and&nbsp;
                <a href={props.links[2]}>Express</a> 
            </h1>
        </div>
    )
}

module.exports = About;