import logging

from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['GET', 'POST'])
def evaluateFixedRace():

        data = request.get_data(as_text=True)
        logging.info("My result :{}".format(data))
        return data
