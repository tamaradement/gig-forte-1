import './App.css';
import React from 'react';


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      tunes: [],
      dropdownIsClicked: false,
      dropdownText: "Search by..."

    }

    this.handleSuccess = this.handleSuccess.bind(this);
    this.handleError = this.handleError.bind(this);
  }

  componentDidMount() {
    // fetch(`${TUNE_LIST_ADDRESS}/tunes_api/`)
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

  handleDropdownClick = (event) => {
    event.preventDefault();
    this.setState({
      dropdownIsClicked: !this.state.dropdownIsClicked,
    });
  }

  handleOptionSelect = (event) => {
    event.preventDefault();
    this.setState({
      dropdownIsClicked: false,
      dropdownText: event.target.innerHTML,
    });
  }

  handleError(error) {    
    this.setState({
      header: 'Something went wrong...'
    })
    console.log(error);
  }

  render() {
    const tunes = this.state.tunes.map((tune) => {
      return (
        <div className='tune-container'>
          <h2>
            {/* <a href={`https://www.gigforte.com/tunes/${tune.id}`}>{tune.title}</a> */}
            {/* <a href={`http://127.0.0.1:8000/tunes/${tune.id}`}>{tune.title}</a> */}
            <a href={`%TUNE_LIST_ADDRESS%${tune.id}`}>{tune.title}</a>
          </h2>
          <p>{tune.composer} | {tune.key}</p>
        </div>
      );
    });

    // const dropdownOptions = searchOptions.map((item, i) => {
    //   return (<p key={i} onClick={this.handleOptionSelect}>{item}</p>);
    // });

    return (
      <div>
        <h1>Tune List</h1>
        {/* <div className="dropdown-container">
          <button onClick={this.handleDropdownClick}>{this.state.dropdownText}</button>
          {this.state.dropdownIsClicked ? dropdownOptions : ''}
        </div> */}
        {tunes}
      </div>   
    );
  }
}
export default App;

// const searchOptions = [
//   "Composer",
//   "Genre",
//   "Title",
// ];
