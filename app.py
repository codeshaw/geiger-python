from geiger import geiger

import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
