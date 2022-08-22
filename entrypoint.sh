#!/bin/bash

# Running our application wigh GUnicorn WSGI server...
gunicorn -b 0:5000 -w 4 app:app
