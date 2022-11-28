FROM ubuntu

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    nginx \
    python3-dev \
    build-essential

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN apt-get -y install python3-pip
RUN pip3 install -r requirements.txt --src /usr/local/src

COPY . .

EXPOSE 5000
CMD [ "python3", "flaskapi.py" ]