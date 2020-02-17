import json
import logging
from flask import jsonify, request
from geiger import geiger

logger = logging.getLogger(__name__)

cpm = 0
acpm = 0.0
uSv = 0.0

@geiger.route('/log', methods=['GET'])
def index():
  if 'CPM' in request.args and 'ACPM' in request.args and 'uSV' in request.args:
    global cpm
    global acpm
    global uSv

    cpm = int(request.args['CPM'])
    acpm = float(request.args['ACPM'])
    uSv = float(request.args['uSV'])

    logger.info("CPM:[{0}], Average CPM:[{1:9.3f}], uSV:[{2:9.3f}]".format(cpm, acpm, uSv))
    response = "OK.ERR0"
    return response, 200
  else:
    return "Invalid input", 400

@geiger.route('/api/radiation-levels', methods=['GET'])
def getRadiationLevels():
  result = {"cpm": cpm, "acpm": acpm, "uSv": uSv}
  return json.dumps(result)
