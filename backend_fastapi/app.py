#app.py
"""
At here we will use FastAPI which is very fast as most people introduced
"""
import uvicorn #Use this ulti to run the fas application if need otherwise we can run the app directly with [python app.py]
from fastapi import FastAPI
import requests #use to connect to the google map api
from fastapi.responses import JSONResponse #output result in JSON format
from fastapi.middleware.cors import CORSMiddleware  #use CORSMiddleware to allow the localhost client can connect to local server when testing
from decouple import config #this lib hels us easily read config data from .env file (pip install python-decouple)


PORT         = int(config('PORT')) #server running on this port
MAP_API_KEY  = config('MAP_API_KEY') #user for mapping API access
ACCESS_TOKEN = config('API_ACCESS_TOKEN') #At this project we have fixed the access token in ACCESS_TOKEN in the .env file (use when we want to check user credentials)

place_search_endpoint = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
place_detail_endpoint = 'https://maps.googleapis.com/maps/api/place/details/json'

app = FastAPI()
origins = [
    "http://localhost",
    "http://127.0.0.1:3006",
    "http://localhost:3006",
    "http://localhost:{}".format(PORT),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""@app.errorhandler(404) #404 error handler
def page_not_found(e):
    error = {'error': 404, 'message': 'You have accessed to wrong path'}
    return response_render(error)

@app.errorhandler(500) #500 error handler
def internal_error(e):
    error = {'error': 500, 'message': 'Something wrong happened, please try again'}
    return response_render(error)"""

@app.get('/api/v1/place/detail/phone/{input_address}')
async def get_place_phone(input_address: str):
    """GET place phone number (might includes some another information)"""

    if check_map_api_key() == False:
        return response_render({'error': 404, 'message': 'Map Key Not found!', "success": False})

    place_id    = find_place_internal(input_address) #get place id
    data        = get_place_detail_phone(place_id) #get place detail from place id then get phone number
    if data is None:
        result  = {'error': 404, 'message': 'Not found', "success": False}
    else:
        result = {"success": True, "message":"Get data completed", "data": data}
    return response_render(result)


@app.get('/api/v1/place/detail/{place_id}')
def get_place_detail(place_id: str):
    """GET place phone number from place id"""

    if check_map_api_key() == False:
        return response_render({'error': 404, 'message': 'Map Key Not found!', "success": False})

    result = get_place_detail_phone(place_id)

    #print(result) #use for debuging

    return response_render(result)


@app.get("/api/v1/place/search/{input_address}")
def find_place(input_address: str):
    """GET place information from an address"""

    if check_map_api_key() == False:
        return response_render({'error': 404, 'message': 'Map Key Not found!', "success": False})

    result = find_place_internal(input_address)

    return JSONResponse(result);


"""
This function get phone number (also include: name, address) from googleapis base on place id
return formatted_phone_number (eg. 024 7300 1828)
"""
def get_place_detail_phone(place_id):
    url           = place_detail_endpoint + '?placeid={}&key={}&fields=formatted_phone_number%2Cformatted_address%2Cname'.format(place_id, MAP_API_KEY)

    payload       = {} #use if we want to pass specific params to the API
    headers       = {} #use if we want to set a particular header param to the API

    response      = requests.request("GET", url, headers=headers, data=payload)
    json_response = response.json()
    if json_response['status'] == "OK":
        result    = json_response['result']
        print(result) #show on the terminal for debuging
        return result
    return None


"""
This function search a place from input string (name or address) and return place id in place_id field
"""
def find_place_internal(input_address):
    inputtype     = 'textquery' #type of search query

    #will search places with result includes: formatted_address, name, geometry, place_id -> this most important that will be use to get the place details.
    url            = place_search_endpoint + "?input={}&inputtype={}&fields=formatted_address%2Cname%2Cgeometry%2cplace_id&key={}".format(input_address, inputtype, MAP_API_KEY)

    payload        = {} #use if we want to pass specific params to the API
    headers        = {} #use if we want to set a particular header param to the API

    response       = requests.request("GET", url, headers=headers, data=payload) #the response will be string in json format
    json_response  = response.json()
    if json_response['status'] == "OK":
        candidates = json_response['candidates']
        #print(candidates)
        if (len(candidates) > 0):
            return candidates[0]["place_id"]  #return place_id from the top item in the list
    return None


"""
This function accept ouput string in json format then return to client with json data type in response header
"""
def response_render(result):
   
    return JSONResponse(result)

def check_map_api_key():
    """Check google map API key setting in .env file"""
    if MAP_API_KEY == "fill_your_api_key_here" or MAP_API_KEY == None:
        return False
    return True      

#Server running functions =================================================================>
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=int(PORT))
    print("The server is running on port " + PORT)

#================= EOF server running =====================================================<    