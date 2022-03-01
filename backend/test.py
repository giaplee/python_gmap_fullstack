#test.py
import requests #use to connect to the google map api
import unittest
from decouple import config #this lib hels us easily read config data from .env file (pip install python-decouple)

class DoTheTestCase(unittest.TestCase):
    def test_case_get_phone(self):
        payload        = {} #use if we want to pass specific params to the API
        headers        = {} #use if we want to set a particular header param to the API
        #test address: 1401 N Shoreline Blvd, Mountain View, CA 94043, USA
        #test result expectation in formatted_phone_number: (650) 810-1010
        backend_port   = int(config('PORT'))
        backend_url    = ' http://localhost:{}/api/v1/place/detail/phone/Computer%20History%20Museum%20Mountain%20View%20USA'.format(backend_port)
        response       = requests.request("GET", backend_url, headers=headers, data=payload) #the response will be string in json format
        json_response = response.json()
        print(json_response)
        formatted_phone_number = json_response["data"]["formatted_phone_number"]
        self.assertEqual("(650) 810-1010", formatted_phone_number, "Check the return result")

if __name__ == '__main__':
    unittest.main()