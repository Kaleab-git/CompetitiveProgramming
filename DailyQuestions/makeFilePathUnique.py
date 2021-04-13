class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_set = set()
        unique_names = {}
        ans = []
        for name in names:
            if name in unique_names:
                k = unique_names[name]
                while f"{name}({k})" in unique_names:
                    k+=1
                ans.append(f"{name}({k})")
                unique_names[f"{name}({k})"] = 1
                unique_names[name] = k
            else:
                unique_names[name] = 1
                ans.append(name)
        return ans
        
        