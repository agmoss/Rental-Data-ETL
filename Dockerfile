FROM ubuntu:latest

# Install Python.
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Dependency for mysql-connector
RUN apt-get install -y default-libmysqlclient-dev

# For sending data to MYSQL Cloud DB
EXPOSE 3306 465 587 25

# Copy the app files to a folder and run it from there
WORKDIR /app
ADD . /app

RUN chmod g+w /app

# Make sure dependencies are installed
RUN pip3 install -r requirements.txt

# Run the app
CMD ["python", "app.py", "05:30"]