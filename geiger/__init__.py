from flask import Flask

geiger = Flask(__name__)

from geiger import routes