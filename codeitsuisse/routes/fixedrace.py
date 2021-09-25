import logging

from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluateFixedRace():

    # logging.info("data sent for evaluation {}".format(data))

        data = request.get_data()
        logging.info("My result :{}".format(data))
        return data
        # for i in data.split(','):
        #     if i in map:
        #         map.update({i, map[i]})
        #     else:
        #         map.update({i, 1})
