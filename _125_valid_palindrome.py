class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        leftP = 0
        rightP = -1
        for char in s:
            if char.isalnum() == True:
                ans.append(char.lower())
                rightP += 1
        while leftP < rightP:
            if ans[leftP] != ans[rightP]:
                return False
            else:
                leftP += 1
                rightP -= 1
        return True
