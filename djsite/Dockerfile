#Pull a pre-built alpine docker image with nginx and python3 installed
FROM tiangolo/uwsgi-nginx:python3.6-alpine3.7

# Set the port on which the app runs; make both values the same.
#
# IMPORTANT: When deploying to Azure App Service, go to the App Service on the Azure 
# portal, navigate to the Applications Settings blade, and create a setting named
# WEBSITES_PORT with a value that matches the port here (the Azure default is 80).
# You can also create a setting through the App Service Extension in VS Code.
ENV LISTEN_PORT=8000
EXPOSE 8000

# Indicate where uwsgi.ini lives
ENV UWSGI_INI uwsgi.ini

# Tell nginx where static files live
ENV STATIC_URL /app/staticfiles

# Copy the app files to a folder and run it from there
WORKDIR /app
ADD . /app

RUN chmod g+w /app

RUN apk add mariadb-client
# RUN apk add py-mysqldb
# RUN apk -q --no-cache add mariadb-client-libs
RUN apk add --no-cache mariadb-dev build-base

# Make sure dependencies are installed
RUN python3 -m pip install -r requirements.txt

run echo > /etc/nginx/conf.d/nginx.conf $'server {\n\
    listen 8000;\n\
    location / {\n\
        include uwsgi_params;\n\
        uwsgi_pass unix:///tmp/uwsgi.sock;\n\
    }\n\
    location ^~ /static {\n\
       alias /app/staticfiles;\n\
    }\n\
}\n\
'