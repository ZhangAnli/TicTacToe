import logging

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

    if strLen == 0:
        return result

    if strLen < 3:
        return [1,0]

    for i in range(strLen):

        left = i - 1
        right = i + 1
        if left >= 0 and right < strLen and s[left] == s[right] and s[left] == s[i]:
            total_score = 0
        else:
            total_score = 1
        firstRd = True

        while left >= 0 and right < strLen:

            if s[left] != s[right]:
                break

            if firstRd and s[left] == s[i]:
                score = 3
            else:
                score = 2

            while left - 1 >= 0 and s[left - 1] == s[left]:
                left -= 1
                score += 1
            while right + 1 < strLen and s[right + 1] == s[right]:
                right += 1
                score += 1

            if score >= 10:
                total_score += score * 2
            elif score >= 7:
                total_score += score * 1.5
            elif  score <= 6:
                total_score += score * 1

            left -= 1
            right += 1
            firstRd = False

        if total_score > result[0]:
            result = [total_score, i]

    return result
