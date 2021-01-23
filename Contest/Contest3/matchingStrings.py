def matchingStrings(strings, queries):
    answer = []
    for q in queries:
        count = 0
        for s in strings:
            if q == s:
                count += 1
        answer.append(count)
    return answer



#map is a good idea for this question.
#instead of iterating through the list for every element and have an O(n*m). 
#you can do this in O(n+m)
#all you have to do is have go through a list one
#if you've seen the charachter add to it's count. If you haven't initiate it with count 1
# You go through your first string O(n). Then you're going to go thourgh queries and see if the items there have counts. If they dont
# then we haven't seen them before.