import {Input, Button, Table, Alert, Spin  } from 'antd';
import React, {useState, useEffect} from 'react';
import axios from 'axios';

//This is a function component
export function Search() {
    const [searchText, setSearchText] = useState(''); //this state is used to store the search text
    const [isInputEmpty, setIsInputEmpty] = useState(false); //this state is used to know user input is empty or not
    const [isError, setIsError] = useState(false); //this state is used to detach the error state which will be return from backend
    const [message, setMessage] = useState(''); //this state is used to set the message in alert box
    const [isLoading, setIsLoading] = useState(false); //this state is used to detect the state of the data request progress to show the loading spin or hide it.
    const [items, setItems] = useState([]); //this state is used to store the return data which will be used in data table to show the result to user

    const columns = [
        {
          title: 'Name',
          dataIndex: 'name',
          key: 'name',
          render: text => <b>{text}</b>,
        },
        {
          title: 'Phone number',
          dataIndex: 'formatted_phone_number',
          key: 'formatted_phone_number',
        },
        {
          title: 'Address',
          dataIndex: 'formatted_address',
          key: 'formatted_address',
        }];

    //This function used for performce a request to backend server where will check then return a item in json format
    const search = () => {
        setIsError(false);
        setIsLoading(true); //show the loading spin
        axios.get(`http://localhost:5005/api/v1/place/detail/phone/${searchText}`)
        .then(res => {
            let data = res.data;
            if (data.success) {
                let items_ = data.data;
                items_.key = Date.now();
                console.log([items_]);
                setItems([items_]);
            }else{
                setIsError(true);
                setMessage(data.message);
            }
            setIsLoading(false); //hide the loading spin
        }).catch(err => {
            setIsLoading(false); //hide the loading spin
            setMessage(err.message);
            setIsError(true);
        })
    };

    //This function will handle and get inputted text from search box
    //We can use require and input validate feature to do the input checking instead of do it manualy
    const getSearchText = (event) => {
        let search_text = event.target.value;
        if (search_text === '' || !search_text) {
            setMessage('Please input search text');
            setIsInputEmpty(true) //will set empty state = TRUE to isInputEmpty flag which will use to make a decision to show inputting warning or not
        }else{
            setSearchText(search_text);
            setIsInputEmpty(false) //set TRUE that means user has inputted search text
        }
    }
    
    useEffect(() => {
        document.title = "FunnelBeam Test project - Seach with Google Map API";
        console.log('Search string = ' + searchText); //show search string in the log windows >> just used for testing
    });

    return (
        <div className="search-detail">
                    <Input.Group compact>
                    <Input style={{ width: 'calc(60%)' }} defaultValue="" 
                            placeholder='Input place name or address here' 
                            type="text" id='search_input'
                            require
                            onChange={(event) => getSearchText(event)} onKeyPress={(e) => e.key ==='Enter' && search()} />
                        
                    <Button type="primary" onClick={() => search()}>Search</Button>
                    {
                            (isInputEmpty || isError) ?
                                <Alert
                                message=""
                                description={message}
                                type="warning"
                                style={{ width: 'calc(60%)'},{height: '50px'}}
                                />   
                            :
                            <span></span>
                        }
                    </Input.Group>
                    
                    <br/>
                    <Spin tip="Loading..." spinning={isLoading}>
                        <Table columns={columns} dataSource={items} key={items.length} />
                    </Spin>
                    
            </div>
    );
}