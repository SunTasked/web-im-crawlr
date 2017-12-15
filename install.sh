#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# add mongo repo gpg key and repo
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list

# packages.
apt-get update
apt-get install docker.io htop
apt-get -y install python-dev python-pip python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev python3 python3-dev

# python modules
pip install --upgrade pip
pip install scrapy pymongo wget

# mongo docker server and local client
apt-get install -y mongodb-org
mkdir -p /vagrant/database/data
docker pull mongo:3.6.0