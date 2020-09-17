#!/bin/bash

python3 manage.py db upgrade
gunicorn -w 2 -b 0.0.0.0:9001 app:app