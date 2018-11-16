import React, { Component } from 'react';

class Title extends Component {
  render() {

    const titleStyle = {
      fontFamily: 'Helvetica',
      color: 'blue',
      fontSize: 18,
      textDecoration: 'underline'
    };

    return (
      <div className="Title" style={titleStyle}>
        <div>
          <h1>My Favorite WebVR Sites</h1>
          <h3>Look at these cool sites:</h3>
        </div>
      </div>
    );

  }
}

export default Title;
