# Use an official Python runtime as a parent image
FROM python:3.6.1-alpine

ARG env

ADD requirements.txt /tmp/${env}.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r /tmp/${env}.txt

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./{{cookiecutter.project_slug}} /app
