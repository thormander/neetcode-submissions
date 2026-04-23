class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # when mid is in left side
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]: # search right
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target or nums[right] < target: # search left
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1

            

'''
[3,4,5,6,1,2]
 l.        r

logn --> binary search as we are sorted

figure out what side we are one: left sorted side or right sorted side.


'''
        