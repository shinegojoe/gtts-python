FROM ubuntu:18.04

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY src/main.py ./src/main.py
COPY .env ./

RUN apt update
RUN apt install curl -y
RUN apt-get install python3-pip -y
RUN pip3 install flask
RUN pip3 install python-dotenv
RUN pip3 install gtts
RUN curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt-get install -y nodejs
RUN apt install vim -y
RUN apt-get install build-essential -y
RUN npm install pm2 -g

# Make port available to the world outside this container
EXPOSE 7001

