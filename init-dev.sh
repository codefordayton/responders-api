#!/usr/bin/env bash

cd `dirname $0`

# Break on error
set -e

# Prefix commands with sudo on Linux platforms
SUDO=""
PLATFORM=`uname`
if [ "$PLATFORM" == "Linux" ] ; then
    sudo yum install postgresql-devel python-devel -y
    SUDO="sudo"
fi

virtualenv .env
.env/bin/pip install -r requirements.txt

${SUDO} docker-compose up -d
~                                
