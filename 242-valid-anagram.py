class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = { }
        for letter in s:
            if letter in anagram_dict:
                anagram_dict[letter] = anagram_dict[letter] + 1
            else:
                anagram_dict[letter] = 1
        for letter in t:
            if letter in anagram_dict:
                anagram_dict[letter] = anagram_dict[letter] - 1
            else:
                return False
        for val in anagram_dict.values():
            if val != 0:
                return False
        return True