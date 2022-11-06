import './App.css';
import React from 'react';


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      tunes: [],
      header: 'Tune List'
    }

    this.handleSuccess = this.handleSuccess.bind(this);
    this.handleError = this.handleError.bind(this);
  }

  componentDidMount() {
    
    fetch("https://www.gigforte.com/tunes/tunes_api/")
    // fetch("http://127.0.0.1:8000/tunes/tunes_api/")
      .then((response => response.json()))
      .then(this.handleSuccess, this.handleError);
  }

  handleSuccess(response) {
    this.setState({
      tunes: response
    })
  }

  handleError(error) {
    
    this.setState({
      header: 'Something went wrong...'
    })
    console.log(error);
  }

  render() {
    const tunes = [];
    for (let i = 0; i < this.state.tunes.length; i++) {
      const tune = this.state.tunes[i];
      tunes.push(
        <h2>
          <a href={`https://www.gigforte.com/tunes/${tune.id}`}>{tune.title}</a>
          {/* <a href={`http://127.0.0.1:8000/tunes/${tune.id}`}>{tune.title}</a> */}
        </h2>
      );
    }

    return (
      <div>
        <h1>{this.state.header}</h1>
        {tunes}
      </div>   
    );
  }
}
export default App;
