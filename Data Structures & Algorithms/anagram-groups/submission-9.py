class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        d = {}
        for word in strs:
            init = [0]*26
            for x in word:
                init[ord(x)-97] +=1
            
            if "".join(str(init)) in d:
                d["".join(str(init))].append(word)
            else:
                d["".join(str(init))] = [word]
        ans = [d[x] for x in d]
        return ans