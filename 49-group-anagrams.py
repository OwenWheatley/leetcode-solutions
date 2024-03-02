class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = { }
        for value in strs:
            tmp = "".join(sorted(value))
            print(tmp)
            if tmp in dict:
                dict[tmp] =  dict[tmp] + [value]
            else:
                dict[tmp] = [value]
        return dict.values()
        