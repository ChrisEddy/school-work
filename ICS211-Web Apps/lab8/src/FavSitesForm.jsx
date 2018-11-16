import React, { Component } from 'react';
import FavSites from './FavSites'

class FavSitesForm extends Component {

  constructor(props) {
    super(props);
    this.state = {
      sites: [],
      checkboxGroup: [false, false, false, false, false],
      showForm: true
    };
    this.handleChange = this.handleChange.bind(this);
    this.submit = this.submit.bind(this);
  }

  handleChange(index) {
    let tempArray = this.state.checkboxGroup;
    if (this.state.checkboxGroup[index]) {
      tempArray[index] = false;
      this.setState({checkboxGroup: tempArray});
    }
    else {
      tempArray[index] = true;
      this.setState({checkboxGroup: tempArray});
    }
    console.log(this.state.checkboxGroup)
  }

  submit() {
    let id;
    for (let i = 0; i < this.state.checkboxGroup.length; i++) {
      id = i + 1;
      if (this.state.checkboxGroup[i]) {
        this.patchJSON(id, true)
      }
      else {
        this.patchJSON(id, false)
      }
    }
    this.updateSites();
    this.setState({
      showForm: false
    });
  }

  patchJSON(id, boolean) {
    fetch(`http://localhost:3000/sites/${id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "checked": boolean
      })

    }).then(response => this.handleHTTPErrors(response))
      .then(result => {
        this.updateSites();
      })
      .catch(error => {
        console.log(error);
      });
  }

  handleHTTPErrors(response) {
    if (!response.ok) throw Error(response.status +
      ': ' + response.statusText);
    return response;
  }

  componentDidMount() {
    this.updateSites();
  }

  updateSites() {
    fetch('http://localhost:3000/sites')
      .then(response => this.handleHTTPErrors(response))
      .then(response => response.json())
      .then(result => {
        this.setState({
          sites: result
        });
      })
      .catch(error => {
        console.log(error)
      })
  }

  render() {

    const formStyle = {
      backgroundColor: 'lightblue',
      marginLeft: '-200px',
      height: '50vh',
      width: '100vw',
      borderRadius: '50px'
    };
    const pStyle = {
      color: 'red',
      display: 'inline',
      margin: '20px'
    };
    const inputStyle = {
      height: '30px',
      width: '60px',
    };
    const buttonStyle = {
      height: '30px',
      width: '60px',
      color: 'white',
      backgroundColor: 'blue',
      borderRadius: '20px',
      marginLeft: '40vw',
      marginTop: '10vh'
    };

    if (this.state.showForm === false) {
      return (
        <FavSites/>
      );
    }
    else {
      return (
        <div className="FavSitesForm">
          <div style={formStyle}>
            <h2 style={{"textAlign": "center"}}>Choose your website!</h2>
            <p style={pStyle}>Solar System</p>
            <input style={inputStyle} onChange={() => this.handleChange(0)} checked={this.state.checkboxGroup[0]}
                   type="checkbox" name="SolarSystem" value="0"/>
            <p style={pStyle}>Gunters of Oasis</p>
            <input style={inputStyle} onChange={() => this.handleChange(1)} checked={this.state.checkboxGroup[1]}
                   type="checkbox" name="Gunters" value="1"/>
            <p style={pStyle}>A-Painter</p>
            <input style={inputStyle} onChange={() => this.handleChange(2)} checked={this.state.checkboxGroup[2]}
                   type="checkbox" name="A-Painter" value="2"/>
            <p style={pStyle}>Reddit</p>
            <input style={inputStyle} onChange={() => this.handleChange(3)} checked={this.state.checkboxGroup[3]}
                   type="checkbox" name="Reddit" value="3"/>
            <p style={pStyle}>Google</p>
            <input style={inputStyle} onChange={() => this.handleChange(4)} checked={this.state.checkboxGroup[4]}
                   type="checkbox" name="Google" value="4"/>
            <br/>
            <input style={buttonStyle} onClick={() => this.submit()} type="submit" value="Submit"/>
          </div>
        </div>
      );
    }
  }
}

export default FavSitesForm;
