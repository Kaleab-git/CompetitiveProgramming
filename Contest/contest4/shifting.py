class Solution:
    def shiftingLetters(self, S, shifts):
       for index, x in enumerate(shifts):
           S = self.shift(S, x, index)
       return S

    def shift(self, string, x, length):
        newString = ""
        for i in range(len(string)):
            if i < length + 1:
                if ord(string[i]) + x > 122:
                    # print(f"chr:{chr(ord('a') + (x-(ord('z')-ord(string[i]))))}. ord: {ord('a') + (x-(ord('z')-ord(string[i])))}")
                    newString += chr(ord('a') + (x-(ord('z')-ord(string[i]))))
                else:
                    newString += chr(ord(string[i]) + x)
            else:
                newString += string[i]
        return newString


sol = Solution()

print (sol.shiftingLetters("abc", [3,5,18]))