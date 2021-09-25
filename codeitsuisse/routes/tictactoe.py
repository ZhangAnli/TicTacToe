import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tictactoe', methods=['POST'])
def evaluateTicTacToe():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    # My code
    battleId = data.get("battleId")
    # Return result
    result = battleId
    logging.info("My result :{}".format(result))
    return json.dumps(result)

