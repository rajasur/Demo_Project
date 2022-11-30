FROM python:3.7


#RUN apt-get update
#RUN apt-get install python3

#RUN apt-get install python3

#RUN apt-get -y install \
#    nginx \
#    python3-dev \
#   build-essential

WORKDIR /app

COPY requirements.txt /app/requirements.txt
#RUN apt-get -y install python3-pip
RUN pip3 install -r requirements.txt --src /usr/local/src

COPY . .

EXPOSE 5000
CMD [ "python3", "flaskapi.py" ]