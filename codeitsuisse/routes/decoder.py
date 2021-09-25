import logging
import random

from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['GET', 'POST'])
def evaluateFixedRace():

        data = request.get_json()

        possible_values = data["possible_values"]
        num_slots = data["num_slots"]
        history = data["history"]

        result = [{
                "answer": calculate(possible_values, num_slots, history)
        }]

        logging.info("My result :{}".format(data))
        return jsonify(result)

def calculate(values, slots, history):
        result = []
        for i in range(slots):
                result.append(random.choice(values))