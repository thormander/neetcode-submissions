class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            current_sum = numbers[right] + numbers[left]

            if current_sum == target:
                return [left+1,right+1]
            elif current_sum > target:
                right -= 1
            else:
                left += 1
        


'''
indexes cant be equal, return index+1

O(1) space --> use existing input and work off that

[1,2,3,4]
 |   |

is current sum > or < target?
    - less, move left pointer right
    - greater, move right pointer left
'''