import logging
import json

from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluateAsteroid():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    test_cases = data.get("test_cases")
    result = []
    for test_case in test_cases:
        s = str(test_case)
        current = {"input":s, "score": calculate(s)[0], "origin": calculate(s)[1]}
        result.append(current)

    logging.info("My result :{}".format(result))
    return jsonify(result)

def calculate(s):

    result = [0, 0]
    strLen = len(s)

    for i in range(strLen):

        left = i
        right = i
        total_score = 0
        multiplier = 1

        while left >= 0 and right < strLen:
            if s[left] != s[right]:
                break




            c = s[left]

            if left == right:
                score = 1
            else:
                score = 2

            if left - 1 >= 0 and right + 1 < strLen and (s[left - 1] == s[left] and s[right + 1] == s[right]):

                while left - 1 >= 0 and s[left - 1] == c:
                    left -= 1
                    score += 1
                while right + 1 < strLen and s[right + 1] == c:
                    right += 1
                    score += 1

            if score >= 10:
                multiplier = 2
            elif score >= 7:
                multiplier = 1.5
            elif  score <= 6:
                multiplier = 1

            total_score += score * multiplier

            left -= 1
            right += 1

        if total_score > result[0]:
            result = [int(total_score), int(i + 1)]

    return result