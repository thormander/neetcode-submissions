class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # key: num | val: index

        for i,v in enumerate(nums):
            potential = target - v

            if potential in hashmap:
                return [hashmap[potential],i]

            hashmap[v] = i
        
        
'''
return index

hashmap = key: num, val: index

target - current num = key to lookup in hashmap

if its in hashmap
    return that index + current index
'''