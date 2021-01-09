class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        h_index_list = []
        if len(citations) == 0:
            return 0
        for n in range (citations[len(citations)-1]+1): #n ranges from 0 to max in citations which is the last element because it's                                                             sorted.
            count = 0
            for i in citations:
                if n <= i:
                    count += 1
            if count >= n: 
                h_index_list.append(n)   
        return h_index_list[len(h_index_list)-1]