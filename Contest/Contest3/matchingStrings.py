def matchingStrings(strings, queries):
    answer = []
    for q in queries:
        count = 0
        for s in strings:
            if q == s:
                count += 1
        answer.append(count)
    return answer