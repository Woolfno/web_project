#!/bin/bash
mkdir -p public/img
mkdir -p public/css
mkdir -p public/js
mkdir -p uploads
mkdir -p etc

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/site-enable/deafault
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
