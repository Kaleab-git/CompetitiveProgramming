class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            letter_map = {}
            mapped_letter = set()
            mapped_pattern = set()
            i=0
            while i < len(word):
                if word[i] in mapped_letter:
                    if letter_map[word[i]] != pattern[i]: break
                else:
                    if pattern[i] in mapped_pattern: break
                    letter_map[word[i]] = pattern[i]
                    mapped_letter.add(word[i])
                    mapped_pattern.add(pattern[i])
                i+=1
            if i==len(word): ans.append(word)
        return ans