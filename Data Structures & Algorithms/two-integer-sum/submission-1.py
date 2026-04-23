class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {} # key: number | value: index

        for i,v in enumerate(nums):
            check = target - v
            
            if check in dictionary:
                return [dictionary[check],i]
            else:
                dictionary[v] = i
        

'''
returning index

in one pass

store seen numbers in a set
as we iterate through check if current number - target is in set
if it is return the pair
if not keep iterating until we hit end and return false

in the set, need to store number and its index (num,index)
    -- use a dict instead with key as number, value as index


'''