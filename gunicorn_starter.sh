#!/bin/sh

gunicorn zeusapi.wsgi -b 0.0.0.0:5000 -w 4 --max-requests 100