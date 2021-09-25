import logging
import random

from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluateFixedRace():
    data = request.get_data(as_text=True)
    logging.info("My result :{}".format(data))
    str = data.split(',')
    random.shuffle(str)
    result = ''
    for i in str:
        result += (i + ',')
    return result[:-1]
