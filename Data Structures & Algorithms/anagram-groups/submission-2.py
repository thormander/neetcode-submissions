class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countToStrings = {} # key: counts | value: [word1,word2,..]

        for s in strs:
   
            # map s to its key/count (populate key)
            key = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                key[index] += 1
            
            # start workign with our dictionary
            key_tup = tuple(key)
            if key_tup in countToStrings:
                countToStrings[key_tup].append(s)
            else:
                countToStrings[key_tup] = [s]
            
        # we have groups, now extract to a list
        return list(countToStrings.values())
        

            



'''
if chars are the same = group them together

count the chars --> not only just count, but need someway to keep the count consistent across different strings
    - use a list full of 0's and index can represent the letter

track count in this list
    - REMEBER we will need to convert list to tuple before using as a key

letter to index? --> ord 

dictionary:

[1,4,0,0,3,...] | [word1,word2]
[0,0,0,1,0,...] | [word3]
'''