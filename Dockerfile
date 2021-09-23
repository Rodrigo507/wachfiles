FROM python:3

# WORKDIR /usr/src/app

# RUN apt-get update \
#     apt-get install vim -y
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /source

WORKDIR /source

COPY ./source /source

# CMD [ "python3", "/source/main.py" ]