class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for x in strs:
            compte = ["0"]*26
            for i in x:
                compte[ord(i)-97] = str(int(compte[ord(i)-97])+1)
            if '-'.join(compte) not in d:
                d['-'.join(compte)] = [x]
            else: d['-'.join(compte)].append(x)

        return [d[x] for x in d]

