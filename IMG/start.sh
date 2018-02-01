#!/bin/bash

# Start Gunicorn process
echo Start Gunicorn.
exec gunicorn IMG.wsgi:application \
     --bind 0.0.0.0:8001 \
     --workers 3

