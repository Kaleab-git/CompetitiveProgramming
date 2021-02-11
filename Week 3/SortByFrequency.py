class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count_dict = {}
        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        print (count_dict)
        for i in count_dict:
            temp = sorted(count_dict, key=count_dict.get)
        result = []
        for i in range(len(temp)):
            for j in range(i, len(temp)):
                if count_dict[temp[i]] == count_dict[temp[j]] and temp[i] < temp[j]:
                    temp[i], temp[j] = temp[j], temp[i]
                    
        for i in range(len(temp)):
            for j in range(count_dict[temp[i]]):
                result.append(temp[i])
        return result

    