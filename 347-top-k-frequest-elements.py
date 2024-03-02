class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = { }
        ans = []
        for value in nums:
            if value in dict:
                dict[value] = dict[value] + 1
            else:
                dict[value] = 1
        print(dict)
        tmp = sorted(dict.items(), key=lambda item: item[1])
        counter = 0
        other = -1
        while counter < k:
            ans.append(tmp[other][0])
            counter = counter + 1
            other = other -1
        return ans