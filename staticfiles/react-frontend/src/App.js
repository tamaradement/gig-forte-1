// import './App.css'
import React, { Component } from 'react';

class Tune extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <h2><a href={`http://www.gigforte.com/tunes/${this.props.tune.id}/`}>{this.props.tune.title}</a></h2>
        <p>{this.props.tune.composer} | {this.props.tune.genre}</p>
      </div>
    );
  }

}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
        isLoading: true,
        tunes: [],
    };

    this.handleSuccess = this.handleSuccess.bind(this);
    this.handleError = this.handleError.bind(this); 
  }
  componentDidMount() {
    fetch("http://www.gigforte.com/tunes/tunes_api/")
      .then((response => response.json()))
      .then(this.handleSuccess, this.handleError);
  }

  handleSuccess(responseData) {
    console.log(responseData);

    this.setState({
      isLoading: false,
      tunes: responseData,
    });
  }

  handleError(error) {
    console.log(error);
    console.log("Some error");
  }

  render() {
    let tuneList = [];
    for (let i = 0; i < this.state.tunes.length; i++) {
      const tune = this.state.tunes[i];
      tuneList.push(<Tune key={i} tune={tune} />);
    }

    return (
      <div>
        <h1>Tune List</h1>
        <br></br>
        {tuneList}
      </div>
    );
  }
}


export default App;
