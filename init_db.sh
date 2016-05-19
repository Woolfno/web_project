#!/bin/bash

mysql -uroot -e "CREATE DATABASE ask;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'box';"
mysql -uroot -e "GRANT ALL ON ask.* TO 'box'@'localhost';"
