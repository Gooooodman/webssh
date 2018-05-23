#!/bin/sh
#

#cd `dirname $0`
pwd


arg1=$1

if [ -z "$arg1" ]; then
arg1='8088'

fi




gunicorn --workers=4 -b 0.0.0.0:$arg1 web.wsgi --threads 40 --max-requests 4096 --max-requests-jitter 512








