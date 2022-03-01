FROM python:alpine3.7 
#FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 5005
ENTRYPOINT [ "python" ] 
CMD [ "app.py"]