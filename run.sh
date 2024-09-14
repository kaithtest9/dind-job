#!/bin/bash
sudo gpasswd -a $USER docker
gpasswd -a docker
sudo service docker start

gunicorn -b :8080 -w 1 app:app