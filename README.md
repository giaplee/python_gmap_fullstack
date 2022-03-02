# python googlemap >> fullstack with reactjs
Demo how to implement google map place API with python (Flask, FastAPI) and reactjs

**`Purpose:`**
- This demo project help you can understand how to implement google map api in a backend REST API to reuse it in other way by you
- At here, we know how to build a REST API with Flask or FastAPI with Python language
- Logic is very simple: we build and expose a api endpoint which will helps the user can search and get a specific phone number (might includes place name, address) from an inputted address or place name on the website with an input box.
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

**`Technical stack:`**
1. Programming language: Python
2. Backend API framework: Flask & FastAPI
3. Containerize with Docker
4. Frontend for API testing: Reactjs with Node
5. Development environment: MacOs
6. Testing environments: MacOS, Linux (Ubuntu 18.04, CentOS 7)
7. Support deploy environments: Linux (Ubuntu 18 - 20, CentOS, Debian), Windows Server with Docker Engine for the Desktop
8. Use NGINX for backend proxy configuration if you want to use the api on your server instance

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

