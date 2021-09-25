import logging
import sys

from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/parasite', methods=['POST'])
def evaluateParasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for test_case in data:
        result.append({
            "room": test_case["room"],
            "p1": calculate(test_case)[0],
            "p2": calculate(test_case)[1],
            "p3": calculate(test_case)[3],
            "p4": calculate(test_case)[4]
        })

    logging.info("My result :{}".format(result))
    return jsonify(result)

def calculate(json_object):

    result = []

    grid = json_object["grid"]
    interested_individuals = json_object["interestedIndividuals"]

    p1 = {}
    for pos in interested_individuals:
        row = pos.split(',')[0]
        col = pos.split(',')[1]
        if grid[row][col] == 0 or grid[row][col] == 2:
            p1[pos] = -1
        else:
            p1[pos] = dfs(grid, row, col, 0)

    result[0] = p1

    return result

def dfs(grid, i, j, time):

    if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] in [0, 2]):
        return -1

    if (grid[i][j] == 3):
        return time

    if (grid[i][j] == 1):
        up = dfs(grid, i - 1, j, time + 1)
        down = dfs(grid, i + 1, j, time + 1)
        left = dfs(grid, i, j - 1, time + 1)
        right = dfs(grid, i, j + 1, time + 1)

        considered = []
        for x in [up, down, left, right]:
            if x > -1:
                considered.append(x)

        return min(considered)
