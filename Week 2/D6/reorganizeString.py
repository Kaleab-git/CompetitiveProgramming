s = "aaaaaaabbbbccc"
l = len(s)
char_dict = {'a':6,'b':4,'c':3}
ch = ['a','b','c']
nl = 0
ns = ""
b = 0; nonb = 1

while nl <= l:
    while len(ch)!=0:
        ns+=ch[b]
        nl+=1
        ns+=ch[nonb]
        nl+=1
        nonb+=1
        print (ns)
    b+=1
    nonb=b+1

print (ns)

























def reorganizeString(S):
    L = len(S)
    s_list = []
    result_list = []

    for i in S:
        s_list.append(i)
    for i in range(L-1):
        if s_list[i] == s_list[i+1]:
            for j in range(i,L): #if the element we find by searching after  i is different from i then swap
                if s_list[j] != s_list[i+1]:
                    s_list[i+1], s_list[j] = s_list[j], s_list[i+1]
    return "".join(s_list)

"""
Version that doesnt work for all test case. 
class Solution(object):
#for n similar charachers we have n-1 spots to fill with a different character
#check if the number of the rest of the characters in >= n-1
#check for as many characters.
    def reorganizeString(self, S):
        character_count_dict = {}
        for i in S:
            if i in character_count_dict:
                character_count_dict[i] += 1
            else:
                character_count_dict[i] = 1
        result = ""
        while len(result) != len(S):
            for key in character_count_dict:
                if character_count_dict[key] != 0:
                    result += key
                    character_count_dict[key] -= 1
        if result[-1] == result[-2]:
            return result
        else:
            return result  
"""
