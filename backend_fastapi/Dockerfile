FROM python:alpine3.7 
#FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt && export $(grep -v '^#' .env | xargs -d '\n') && echo $PORT
EXPOSE 5005
ENTRYPOINT [ "python" ] 
CMD [ "app.py"]
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", $PORT]