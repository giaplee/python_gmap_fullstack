#main
from flask import Flask, jsonify, Response
from flask_cors import CORS
import requests
from decouple import config #this lib helps us easily read config data from .env file (pip install python-decouple)


PORT         = int(config('PORT')) #server running on this port
MAP_API_KEY  = config('MAP_API_KEY') #key for google mapping API access
ACCESS_TOKEN = config('API_ACCESS_TOKEN') #At this project we have fixed the access token in ACCESS_TOKEN in the .env file (use when we want to check user credentials)

place_search_endpoint = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
place_detail_endpoint = 'https://maps.googleapis.com/maps/api/place/details/json'

app  = Flask(__name__)

"""Only allow CORS to all requests for the testing. In fact, we only allow requests from a specific source that we know"""
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) #add CORS handle for localhost testing on different ports

@app.errorhandler(404) #404 error handler
def page_not_found(e):
    error = {'error': 404, 'message': 'You have accessed to wrong path'}
    return response_render(error)

@app.errorhandler(500) #500 error handler
def internal_error(e):
    error = {'error': 500, 'message': 'Something wrong happened, please try again'}
    return response_render(error)

@app.get('/api/v1/place/detail/phone/<string:input_address>')
def get_place_phone(input_address):
    """GET place phone number (might includes some another information)"""

    #check google map key setting first
    if check_map_api_key() == False:
        return response_render({'error': 404, 'message': 'Map Key Not found', "success": False})

    place_id    = find_place_internal(input_address) #get place id
    data        = get_place_detail_phone(place_id) #get place detail from place id then get phone number
    if data is None:
        result  = {'error': 404, 'message': 'Map Key Not found!', "success": False}
    else:
        result  = {"success": True, "message":"Get data completed", "data": data}
    return response_render(result)


@app.get('/api/v1/place/detail/<string:place_id>')
def get_place_detail(place_id):
    """GET place phone number from place id"""

    #check google map key setting first
    if check_map_api_key() == False:
        return response_render({'error': 404, 'message': 'Map Key Not found!', "success": False})

    result = get_place_detail_phone(place_id)

    print(result)

    return response_render(result)


@app.get("/api/v1/place/search/<string:input_address>")
def find_place(input_address):
    """GET place information from an address"""

    if check_map_api_key() == False:
        return response_render({'error': 404, 'message': 'Map Key Not found!', "success": False})

    result = find_place_internal(input_address)

    return response_render(result);


"""
This function get phone number from googleapis base on place id
return formatted_phone_number (eg. 024 7300 1828)
"""
def get_place_detail_phone(place_id):
    url           = place_detail_endpoint + '?placeid={}&key={}&fields=formatted_phone_number%2Cformatted_address%2Cname'.format(place_id, MAP_API_KEY)

    payload       = {} #use if we want to pass specific params to the API
    headers       = {} #use if we want to set a particular header param to the API

    response      = requests.request("GET", url, headers=headers, data=payload)
    json_response = response.json()
    #print(json_response)
    if json_response['status'] == "OK":
        result    = json_response['result']
        print(result)
        return result
    return None


"""
This function search a place from input string (name or address) and return place id in place_id field
"""
def find_place_internal(input_address):
    inputtype     = 'textquery' #type of search query

    #will search places with result includes: formatted_address, name, geometry, place_id -> this most important that will be use to get the place details.
    url           = place_search_endpoint + "?input={}&inputtype={}&fields=formatted_address%2Cname%2Cgeometry%2cplace_id&key={}".format(input_address, inputtype, MAP_API_KEY)

    payload       = {} #use if we want to pass specific params to the API
    headers       = {} #use if we want to set a particular header param to the API

    response      = requests.request("GET", url, headers=headers, data=payload) #the response will be string in json format
    json_response = response.json()
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
    return jsonify(result)

def check_map_api_key():
    """Check google map API key setting in .env file"""
    if MAP_API_KEY == "fill_your_api_key_here" or MAP_API_KEY == None:
        return False
    return True    

#Server running functions =================================================================>
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)

#================= EOF server running =====================================================<    