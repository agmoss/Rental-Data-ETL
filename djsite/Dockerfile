FROM python:3.7

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/djsite

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    libffi-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools \
    vim \
    nginx

RUN service nginx restart
# copy project
COPY . /usr/src/djsite/

# install dependencies
RUN pip install -r requirements.txt