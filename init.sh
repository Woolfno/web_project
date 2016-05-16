#!/bin/bash
mkdir -p public/img
mkdir public/css
mkdir public/js
mkdir uploads
mkdir etc

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/site-enable/deafault
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
