#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo "starting mongodb container ..."
if [ ! "$(docker ps -q -f name=mongodb)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=mongodb)" ]; then
        echo "waking up mongodb container ..."
        docker start mongodb
    else
        echo "runing docker container..."
        docker run -d -p 27017:27017 -v /vagrant/database/data:/data/db --name mongodb mongo:3.6.0
        mongo webimages --eval "db.images.createIndex( { url: 1 } )"
    fi
    echo "mongodb container up and running"
else
    echo "mongodb container already running"
fi

