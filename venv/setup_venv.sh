#!/bin/bash

set -e  # If occur any error, exit

cd $(dirname $0) && cd ..

echo "Installing python requirements"
pip install -r venv/requirements.txt --download-cache=/var/tmp

echo "Installing bower requirements"
bower install

if [ ! -d src/lib ]; then
    echo "Creating Lib symlink"
    ln -s $VIRTUAL_ENV/lib/python2.7/site-packages/ src/lib
fi

if [ ! -d src/apps ]; then
    echo "Creating Apps symlink"
    ln -s $(pwd)/apps/ src/apps
fi