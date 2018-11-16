import React, {Component} from 'react'
import Title from './Title/Title.jsx'
import Site from './Site.jsx'

class FavSites extends Component {

  constructor(props){
    super(props);
    this.state = {
      sites: []
    };
  }

  componentDidMount(){
    this.updateSites()
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

  handleHTTPErrors(response) {
    if (!response.ok) throw Error(response.status +
      ': ' + response.statusText);
    return response;
  }

  render() {
    const favSitesStyle = {
      height: 300,
      width: 600,
      padding: 20,
      backgroundColor: '#FFF2CC',
      boxShadow: '0px 0px 5px #666'
    };

    return (
      <div style={favSitesStyle}>
        <Title/>
        <ol>
          {this.state.sites.map(sites =>
            <Site key={sites.id} checked={sites.checked} Title={sites.name} Link={sites.link}
                  SiteColor={{color: sites.color}}/>
          )}
        </ol>
      </div>
    )
  }
}

export default FavSites;
