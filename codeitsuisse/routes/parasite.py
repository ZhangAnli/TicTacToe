import logging
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
            "p1": calculateP1(test_case),
            "p2": 1,
            "p3": 1,
            "p4": 0
        })

    logging.info("My result :{}".format(result))
    return jsonify(result)

def calculateP1(json_object):

    # Initiate variables
    grid = json_object["grid"]
    interested_individuals = json_object["interestedIndividuals"]
    result = {}

    # Convert all 2s to 0s
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                grid[i][j] = 0

    for pos in interested_individuals:
        row = int(pos.split(',')[0])
        col = int(pos.split(',')[1])
        if grid[row][col] == 0:
            result[pos] = -1
        elif grid[row][col] == 3:
            result[pos] = 0
        else:
            path = dfs(grid, row, col, 0)
            if (path == pow(len(grid), 2)):
                result[pos] = -1
            else:
                result[pos] = path

    return result

def dfs(grid, i, j, time):

    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
        return pow(len(grid), 2)

    if (grid[i][j] == 3):
        return time

    if (grid[i][j] == 1):
        grid[i][j] = 0
        result = min(
            dfs(grid, i + 1, j, time + 1),
            dfs(grid, i - 1, j, time + 1),
            dfs(grid, i, j + 1, time + 1),
            dfs(grid, i, j - 1, time + 1),
        )
        grid[i][j] = 1
        return result


