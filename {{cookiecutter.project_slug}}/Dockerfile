# Use an official Python runtime as a parent image
FROM python:3.6.1-alpine

ARG ENV

ADD requirements/${ENV}.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

ADD ./{{cookiecutter.project_slug}} /app
