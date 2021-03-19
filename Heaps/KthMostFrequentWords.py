    import heapq as heap
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        answer = []
        count_dict = {count:[] for count in range(1, len(words)+1)}
        myHeap = []
        words_set = set(words)
        d = {} 
        for i in words:
            d[i] = d.get(i, 0) + 1 
        for i in d:
            count_dict[d[i]].append(i)
        for i in count_dict:
            count_dict[i].sort()
        for i in count_dict.keys():
            heap.heappush(myHeap, -i)
        
        while len(answer) < k:

            Max = -heap.heappop(myHeap)
            if len(answer) + len(count_dict[Max]) <= k:
                answer.extend(count_dict[Max])
            elif len(answer) < k:
                difference = k - len(answer)
                answer.extend(count_dict[Max][:difference])
                
        return answer
        