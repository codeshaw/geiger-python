import logging
import os
from flask import Flask

geiger = Flask(__name__)
from geiger import routes

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
