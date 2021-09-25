import logging
import random

from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/decoder', methods=['POST'])
def evaluateDecoder():
    data = request.get_json()

    possible_values = data.get("possible_values")
    num_slots = int(data.get("num_slots"))
    history = data.get("history")

    result = [{
        "answer": calculate(possible_values, num_slots, history)
    }]

    logging.info("My result :{}".format(data))
    return result


def calculate(values, slots, history):
    result = []
    for i in range(slots):
        result.append(random.choice(values))
    return ["a", "b", "c", "d"]
