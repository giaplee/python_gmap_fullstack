
[![Build Status](https://travis-ci.org/AOEpeople/Tagging.svg?branch=master)](https://#)
[![License](https://img.shields.io/badge/license-MIT%2FApache--2.0-blue)](https://www.apache.org/licenses/LICENSE-2.0)
[![Python version](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue)](https://#)
[![Docker build](https://img.shields.io/badge/docker%20build-automated-066da5)](https://#)
![Python Flask](https://img.shields.io/static/v1?label=Flask&message=Implemented&color=blue)
![Python Flask](https://img.shields.io/static/v1?label=FastAPI&message=Implemented&color=green)
![Python Flask](https://img.shields.io/static/v1?label=Reactjs&message=WebApp&color=informational)
# python googlemap >> fullstack with reactjs
Demo how to implement google map place API with python (Flask, FastAPI) and reactjs

**`Activity Flow Diagram(Sequence)`**
<p align="left">
    <img src="https://github.com/giaplee/python_gmap_fullstack/blob/master/documents/pymap_api_sequence_diagram.png" width="600" />
</p>

**`Purpose:`**
- This demo project help you can understand how to implement google map api in a backend REST API to reuse it in other way by you
- At here, we know how to build a REST API with Flask or FastAPI with Python language
- Logic is very simple: we build and expose an api endpoint which will helps the user can search and get a specific phone number (might includes place name, address) from an inputted address or place name on the website with an input box.
- This is a sample for the result from our API:
-- Eg. The user search the phone with this address: Computer History Museum Mountain View USA
```json
{
    "data": {
        "formatted_address": "1401 N Shoreline Blvd, Mountain View, CA 94043, USA",
        "formatted_phone_number": "(650) 810-1010",
        "name": "Computer History Museum"
    },
    "message": "Get data completed",
    "success": true
}
```
- The main endpoint will be: 
```python
the_endpoint = "http://[domain/localhost]:[port]/api/v1/place/detail/phone/{input_address}"
#Replace [port] with your port in .env file (with key is PORT) 
```

**`Project structure`**
```xml
-root folder
----backend #this folder contains api source that was implemented with Flask
----backend_fastapi #this folder contains api source that was implemented with FastAPI 
----frontend #this fodler contains source web app that was implemented with Reacjs which helps us easily to test the api

#In fact, we just use an Api from backend folder or backend_fastapi because they have same function and logic except one uses Flask and one uses FastAPI
#I have implemeted both framework (Flask and FastAPI) with only purpose is want to know: (which one will run faster or implement easier)
```

**`Technical stack:`**
1. Programming language: Python
2. Backend API framework: Flask & FastAPI ([link](https://fastapi.tiangolo.com/))
3. Containerize with Docker
4. Frontend for API testing: Reactjs with Node
5. Further, we can you Redis caching solution to cache the phone number with key is place _id to reduce request time to Map API
6. Development environment: MacOs
7. Testing environments: MacOS, Linux (Ubuntu 18.04, CentOS 7)
8. Support deploy environments: Linux (Ubuntu 18 - 20, CentOS, Debian), Windows Server with Docker Engine for the Desktop
9. Use NGINX for backend proxy configuration if you want to use the api on your server instance


**`Document with Swagger`**
- The FastAPI framework will automatic generate REST API document web for us (Great!)
- After running the backend_fastAPI, we can go to the API document by `http://localhost:[port]/docs` (default port is 5005)
<p align="left">
    <img src="https://github.com/giaplee/python_gmap_fullstack/blob/master/documents/fasapi__web_docs.png" with="500" />
</p>    


**`Deploy with CI/CD and Docker`**
<p align="center">
    <img src="https://github.com/giaplee/python_gmap_fullstack/blob/master/documents/components_deploy_architecture.png" with="500" />
</p>
- Monitor and Alert with Grafana(https://grafana.com/docs/grafana/latest/introduction/)
<p align="left">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTFWLVg8aAnS8mF_b8lwzW62LddEJAAxHCJaqETsFxWLpUlqz7n_Pn5JIDGSUmyCZigyg&usqp=CAU" width="300" />
</p>

**`Prerequiresit`**
- Install Docker first (The guideline here: https://docs.docker.com/engine/install/)
- Recommend you use Ubuntu or MacOS
- Please notice on .env file in each folder of project (backend, backend_fastapi and frontend): open .env file in backend and backend_fastapi folder and then update your map api key and your port you want or use the default port.
- When you run run.sh script it will build a docker image then start it with `docker run` command. Please look at Dockerfile if you want to edit something like expose port (you also have to edit port in .env file)

**`Quick run the demo with shell script`**
1. Download whole project folders from branch: [quickrundemo] because it has .env file which help you config running port and google map API key) **For data security reason so I can't share my .env file content to everyone!**
2. Suppose you are using Ubuntu or MacOS: In the terminal type: `cd quickrundemo/backend` if you want to run the backend that was built with Flask else `cd quickrundemo/backend_fastapi` if you want to run the backend that was built with FastAPI
then you run the run.sh file with `bash run.sh` and wait the script will builds the docker image and runs it for you
3. Open new terminal window then goto the frontend with `cd quickrundemo/frontend` then run run.sh file and wait the script build and run the frontend web with docker image
4. After that, you open web browser then go to `http://localhost:3006`
5. Input any place name or address in the world you know for testing

`Test on the web UI`
<p align="left">
    <img src="https://github.com/giaplee/python_gmap_fullstack/blob/master/documents/web_ui_result.png" with="600" />
</p>
