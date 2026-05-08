# start with a base python image
FROM python:3.13 

# copies the files in the current dir to a file called /app on the container 
COPY . /app

# makes the working dir /app the file you just copied your app in to
WORKDIR /app

# Installs requirements
RUN pip install -r requirements.txt

# runs app.py with the python command
CMD ["python3", "app.py"]