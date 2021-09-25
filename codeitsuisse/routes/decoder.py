import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def evaluateDecoder():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    possible_values = data.get("possible_values")
    numSlots = data.get("num_slots")
    history = data.get("history")

    result = [
        {
            "answer": calculate(possible_values, numSlots)
        }
    ]

    logging.info("My result :{}".format(result))
    return json.dumps(result)


def calculate(values, slots):
    result = []
    for i in range(slots):
        result.append(values[0])
    return result


