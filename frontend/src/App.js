import './App.css';
import { Empty, Input, Button, Table, Tag, Space, Alert  } from 'antd';
import React, {Component} from 'react';
import axios from 'axios';
import {Search} from './components/search';


class App extends React.Component {
  constructor (props) {
    super(props);
    //this.state = {items: [{name:"Googleplex",address:"1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA", phone:"(650) 253-0000"}]};
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
