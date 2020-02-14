import logging
from flask import jsonify, request
from geiger import geiger

logger = logging.getLogger(__name__)

@geiger.route('/log', methods=['GET'])
def index():
    if 'CPM' in request.args and 'ACPM' in request.args and 'uSV' in request.args:
        cpm = int(request.args['CPM'])
        acpm = float(request.args['ACPM'])
        uSV = float(request.args['uSV'])

        logger.info("CPM:[{0}], Average CPM:[{1:9.3f}], uSV:[{2:9.3f}]".format(cpm, acpm, uSV))
        response = jsonify(success=True)
        response.status_code = 200
        return response
    else:
        return "Invalid input", 400
