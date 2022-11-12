import './App.css';
import React from 'react';
import { searchOptions, searchFormValidations } from './utils'


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      tunes: [],
      dropdownIsClicked: false,
      category: "Search by...",
      searchInput: '',
      filteredTunes: [],
      searchFormErrors: {},

    }
  }

  componentDidMount() {
    fetch("https://www.gigforte.com/tunes/tunes_api/")
    // fetch("http://127.0.0.1:8000/tunes/tunes_api/")
      .then((response => response.json()))
      .then(this.handleSuccess, this.handleError);
  }

  handleSuccess = (response) => {
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
      category: event.target.innerHTML,
    });
  }

  handleSearchInput = (event) => {
    event.preventDefault();
    this.setState({
      searchInput: event.target.value.toLowerCase()
    });
  }

  handleResetClick = (event) => {
    event.preventDefault();
    this.setState({
      filteredTunes: [],
      category: "Search by...",
    });
  }

  searchFormHasError = (fields) => {
    let hasError = false;
    const errorData = {};

    fields.forEach((field) => {
      const name = field.name;
      const error = searchFormValidations[name](field);
      if (error) {
        errorData[name] = error;
      }
    });

    if (Object.keys(errorData).length) {
      this.setState({
        searchFormErrors: errorData,
      })

      hasError = true;
    }

    return hasError;
  }

  handleSearchFormSubmission = (event) => {
    event.preventDefault();
    const category = this.state.category.toLowerCase();
    const searchInput = this.state.searchInput;
    // If we need a reset:
    if (this.state.filteredTunes.length) {
      event.currentTarget[0].value = '';
      this.handleResetClick(event);
      return;
    }

    const fields = Array.from(event.currentTarget).filter((input) => input.innerHTML !== 'Search');

    if (!(this.searchFormHasError(fields))) {
      const filteredTunes = this.state.tunes.filter((tune) => {
        const tuneProperty = tune[category].toLowerCase();
        if (tuneProperty.includes(searchInput)) {
          return tune;
        }
        return false;
      });

      event.currentTarget[0].value = '';
  
      this.setState({
        filteredTunes: filteredTunes,
        searchInput: '',
        category: "Search by...",
        searchFormErrors: {},
      });
    }

  }

  handleError = (error) => {    
    this.setState({
      header: 'Something went wrong...'
    })
    console.log(error);
  }

  render() {
    let data;
    if (this.state.filteredTunes.length) {
      data = this.state.filteredTunes;
    } else {
      data = this.state.tunes;
    }

    const tunes = data.map((tune) => { 
      return (
        <div className='tune-container' key={tune.id}>
          <h2>
            <a href={`https://www.gigforte.com/tunes/${tune.id}`}>{tune.title}</a>
            {/* <a href={`http://127.0.0.1:8000/tunes/${tune.id}`}>{tune.title}</a> */}
          </h2>
          <p>{tune.composer} • {tune.key} • {tune.genre}</p>
        </div>
      );
    });

    const dropdownOptions = searchOptions.map((item, i) => {
      return (
        <p 
          className='search-dropdown-item' 
          key={i} 
          onClick={this.handleOptionSelect}>{item}
        </p>
      );
    });

    return (
      <div>
        <h1>Tune List</h1>
        <div className="parent">
          <div className="flex-child">
            {tunes}
          </div>
          <div className="flex-child">
            <form 
              onSubmit={this.handleSearchFormSubmission} 
              className='form-container'>
              <input 
                onChange={this.handleSearchInput} 
                placeholder='Search tunes...'
                name='input'
                className='form-control'>
                
              </input>
              <p className='error-message'>{this.state.searchFormErrors.input}</p>
              <button 
                name='category' 
                onClick={this.handleDropdownClick}
                className='fbtn btn btn-info dropdown-toggle dropdown-toggle'
                >{this.state.category}
              </button>
              <p className='error-message'>{this.state.searchFormErrors.category}</p>
              {this.state.dropdownIsClicked ? dropdownOptions : ''}
              <button className='btn btn-primary btn-lg submit-button' type='Submit'>{this.state.filteredTunes.length ? "Reset" : "Search"}</button>
            </form>
          </div>      
        </div> 
      </div>
    );
  }
}
export default App;


