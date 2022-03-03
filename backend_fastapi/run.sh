#!/bin/bash
echo "clean old docker image................................"
yes y | docker system prune -a #you can remove (yes y |) command if want to control docker prune by manually
echo "-----------start docker build..."
docker build -t fbmapapi:v1 .
echo "-----------docker build completed >>"
echo "-----------docker run ..."
#you have to change 5005:5005 to the same port at .env and Dockerfile
docker run --rm -p 5005:5005 --name pymapapi_dev fbmapapi:v1 #you can use -d parameter to run the docker in the background mode (in production mode on remote server)
echo "-----------docker run completed"


#===============READ.ME================================================================
#This file only use for local testing purpose
#We will run docker image in github action (CI/CD) configuration file with similar command above(use github runner service inside the backend server instance)