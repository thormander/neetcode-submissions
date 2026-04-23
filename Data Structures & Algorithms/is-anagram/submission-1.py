class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = {}
        chars_t = {}

        # get chars for s
        for char in s:
            if char not in chars_s:
                chars_s[char] = 1
            else:
                chars_s[char] += 1

        # get chars for t
        for char in t:
            if char not in chars_t:
                chars_t[char] = 1
            else:
                chars_t[char] += 1

        # compare
        return chars_s == chars_t

    
'''
2 dictionaries
track char count

compare dictionaries at end
'''