#!/bin/bash
mkdir -p public/img
mkdir -p public/css
mkdir -p public/js
mkdir -p uploads
mkdir -p etc

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default 
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart
