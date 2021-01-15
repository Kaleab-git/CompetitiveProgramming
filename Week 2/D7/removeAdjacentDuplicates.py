class Solution(object):
    def remove_duplicate(self,S):
	    self.l = len(S)
	    for i in range(self.l-1):
		    if S[i] == S[i+1]:
			    return self.remove_duplicate(S[:i]+S[i+2:])
	    return S
   
sol = Solution()

print (sol.remove_duplicate('A'))
#Last solution
"""
class Solution(object):
    def removeDuplicates(self, S):
        #NAD stands for non-duplicate adjacents
        NADs = []
        last_NAD_index = 0
        for i in S:
            if NADs != []:
                if i == NADs[last_NAD_index-1]:
                    NADs.pop()
                    last_NAD_index -= 1
                    continue 
            NADs.append(i)
            last_NAD_index += 1
        return "".join(NADs)
"""
"Second Solution. Works, but takes too long."                   
#My first solution
'''
 def removeDuplicates(self, S):  
        for i in range(len(S)-1):
            #if len(S) == 2 and S[0] == S[1]:
             #   return ""
            print (S)
            if len(S) == 2:# and S[0] != S[1]:
                print (S)
                return S
            if S[i] == S[i+1]:
                S = self.removeDuplicates(S[:i] + S[i+2:])
            else:
                continue
        return S
'''

#
# Khan Academy
# Solve Binary Search
# Solve Remove Duplicates
# Watch and take note from divide and conquer
# MIT Course
# Web Lab Excersice
# Web Personal Website Assignment   
# How is splitting implemented in Python
# What is it's time complexity
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#