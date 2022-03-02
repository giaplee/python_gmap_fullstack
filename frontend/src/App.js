import './App.css';
import React, {Component} from 'react';
import {Search} from './components/search';


class App extends Component {
  constructor (props) {
    super(props);
  };
  
  render() {
    return (
      <div className="App">
        <div className="App-content">
        <div className="search-panel">
            <Search />
        </div>
        </div>
      </div>
    );
};
}
export default App;
