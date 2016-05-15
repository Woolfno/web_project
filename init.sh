#!/bin/bash
mkdir -p public/img
mkdir public/css
mkdir public/js
mkdir uploads
mkdir etc

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/site-enable/deafault.conf
sudo /etc/init.d/nginx restart
