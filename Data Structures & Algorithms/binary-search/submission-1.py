class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # get midpoint
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        
        return -1



'''
logn + sorted --> binary search

start on both ends, take mid --> is it greater or less, greater go right, elss go left

[-1,0,2,4,6,8]
        |
            |


'''