import logging
import sys

from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/parasite', methods=['POST'])
def evaluateAsteroid():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for test_case in data:
        result.append({
            "room": test_case["room"],
            "p1": calculate(test_case)[0],
            "p2": calculate(test_case)[1],
            "p3": calculate(test_case[3]),
            "p4": calculate(test_case)[4]
        })

    logging.info("My result :{}".format(result))
    return jsonify(result)

def calculate(input):

    result = []

    # Part 1
    grid = input["grid"]
    room = input["room"]
    part1 = []
    peoples = []
    for str in input["interestedIndividuals"]:
        row = str.split(',')[0]
        col = str.split(',')[1]
        peoples.append([row, col])

    # Get virus pos
    virusPos = [-1, -1]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 3:
                virusPos = [i, j]


    def dfs(grid, i, j, x, y, time):
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1):
            return -1

        if (i == x and j == y):
            return time

        shortestTime = sys.maxsize

        if (dfs(grid, i + 1, j, x, y, time + 1) != -1):
            shortestTime = min(shortestTime, dfs(grid, i + 1, j, x, y, time + 1))
        elif (dfs(grid, i + 1, j, x, y, time + 1) != -1):
            shortestTime = min(shortestTime, dfs(grid, i + 1, j, x, y, time + 1))
        elif (dfs(grid, i + 1, j, x, y, time + 1) != -1):
            shortestTime = min(shortestTime, dfs(grid, i + 1, j, x, y, time + 1))
        elif (dfs(grid, i + 1, j, x, y, time + 1) != -1):
            shortestTime = min(shortestTime, dfs(grid, i + 1, j, x, y, time + 1))




    return result