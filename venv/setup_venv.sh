#!/bin/bash

set -e  # If occur any error, exit

cd $(dirname $0) && cd ..

pip install -r venv/requirements.txt --download-cache=/var/tmp

if [ ! -d lib ]; then
    ln -s $VIRTUAL_ENV/lib/python2.7/site-packages/ appengine/lib
fi

if [ ! -d apps ]; then
    ln -s ../apps appengine/apps
fi