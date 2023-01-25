# set base image (host OS)
FROM python:3.8.16-bullseye

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY ./src/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt