def calculate(s):

    result = [0, 0]
    strLen = len(s)

    for i in range(strLen):

        left = i - 1
        right = i + 1
        total_score = 0
        firstRd = True

        while left >= 0 and right < strLen:

            if s[left] != s[right] and firstRd:
                total_score = 1
                break
            elif s[left] != s[right] and not firstRd:
                break

            score = 2

            while left - 1 >= 0 and s[left - 1] == s[left]:
                left -= 1
                score += 1
            while right + 1 < strLen and s[right + 1] == s[right]:
                right += 1
                score += 1

            if firstRd:
                if s[left] == s[i]:
                    score += 1
                else:
                    total_score += 1
                firstRd = False

            if score >= 10:
                total_score += score * 2
            elif score >= 7:
                total_score += score * 1.5
            elif  score <= 6:
                total_score += score * 1

            left -= 1
            right += 1

        if total_score > result[0]:
            result = [total_score, i]

    return result
