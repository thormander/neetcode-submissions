class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # key: char count | value: list of anagrams

        # generate key and populate our map
        for string in strs:
            key = [0] * 26 # alphabet

            for char in string:
                index = ord(char) - ord('a')
                key[index] += 1
            
            key_tuple = tuple(key) # key immutable

            if key_tuple not in hashmap:
                hashmap[key_tuple] = [] # instantiate with a empty list
            
            hashmap[key_tuple].append(string)

        # grab values from map
        return list(hashmap.values())

'''
some way to track what anagram matches with each other
    - count char occurances (what letters it has)

hashmap -> key: char counts | value: [anagrams]

1. get char counts of each, add to map

2. get values of the hashmap and put in a list

--> we cant use a list as key as it must be immutable

key
 - a list that represetns alphabet
 - index will follow what letter it is
 - use ord
 - increment +1 if we see a char and use as key in map
'''