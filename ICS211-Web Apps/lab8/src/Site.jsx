import React, { Component } from 'react';

class Site extends Component {

  constructor(props){
    super(props)
  }

  render() {
    if(this.props.checked === true){
    return (
      <div className="Site" style={this.props.SiteColor}>
          <li>{this.props.Title}<a href={this.props.Link}>{this.props.Link}</a></li>
      </div>
    )
    }
    else{
      return(
        null
      )
    }

  }
}

export default Site;
