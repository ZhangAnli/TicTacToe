import logging
import random
from flask import request
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def evaluateDecoder():

    # Initialise variables
    data = request.get_json()
    possible_values = data.get("possible_values")
    num_slots = int(data.get("num_slots"))

    result = [{
        "answer": calculate(possible_values, num_slots)
    }]

    logging.info("My result :{}".format(data))
    return result


def calculate(values, slots):
    result = []
    for i in range(slots):
        result.append(values[0])
    return result
