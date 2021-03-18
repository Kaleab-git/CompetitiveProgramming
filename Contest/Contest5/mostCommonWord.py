class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if paragraph[-1] != ".?!;": paragraph += "."
        count_dict = {}; word = ""
        for i in paragraph:#basic loop, O(n)
            i = i.lower()
            if word and i in "!?',;. ": # linear lookup time because whats in the quotation is independent of the input size
                if word in banned: # O(len(banned)). banned is not dependent of paragraph
                    word = ""
                    continue
                count_dict = self.count(count_dict, word)
                word = ""
            elif i != " ":
                word =  "".join([word, i])
                # word += i
        Max = ("", 0)
        for i in count_dict: # O(len(count_dict)) which is a subset of paragraph. i.e >= len(paragraph). Upper Bound is still O(n)
            if count_dict[i] > Max[1]: Max = (i, count_dict[i])
        return Max[0]
    def count(self, count_dict, word): # O(len(count_dict)) which is a subset of paragraph. i.e >= len(paragraph). Upper Bound is still O(n)
        if word in count_dict: count_dict[word] += 1
        else: count_dict[word] = 1
        return count_dict



# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         if paragraph[-1] != ".?!;": paragraph += "."
#         count_dict = {}; word = ""
#         for i in paragraph:#basic loop, O(n)
#             i = i.lower()
#             if word and i in "!?',;. ": # linear lookup time because whats in the quotation is independent of the input size
#                 if word in banned: # O(len(banned)). banned is not dependent of paragraph
#                     word = ""
#                     continue
#                 count_dict = self.count(count_dict, word)
#                 word = ""
#             elif i != " ":
#                 word += i
#         Max = ("", 0)
#         for i in count_dict: # O(len(count_dict)) which is a subset of paragraph. i.e >= len(paragraph). Upper Bound is still O(n)
#             if count_dict[i] > Max[1]: Max = (i, count_dict[i])
#         return Max[0]
#     def count(self, count_dict, word): # O(len(count_dict)) which is a subset of paragraph. i.e >= len(paragraph). Upper Bound is still O(n)
#         if word in count_dict: count_dict[word] += 1
#         else: count_dict[word] = 1
#         return count_dict