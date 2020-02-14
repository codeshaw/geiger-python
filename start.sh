#!/bin/sh
source venv/bin/activate
exec waitress-serve --port=8080 geiger:geiger
