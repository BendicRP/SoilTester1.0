#!/bin/bash

#  Start of Apache2 - remove Apache2 default index.html page
if [[ ! -f /var/www/html/old.index.html ]] ;then
    mv /var/www/html/index.html /var/www/html/old.index.html
fi

# Move new index.html and dataFile into Apache2
if [[ -f $PWD/index.html ]] ;then
    cp $PWD/index.html /var/www/html/index.html
    cp $PWD/dataFile.txt /var/www/html/dataFile.txt
fi

# Copy Web Application /html/[All Files] to Apache2
cp -r html/* /var/www/html/

