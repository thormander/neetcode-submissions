class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        result = 0

        while left < right:
            currentAmtWater = (right - left) * (min(heights[left],heights[right]))
            result = max(result,currentAmtWater)

            # pointer shift
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        
        return result

'''     
2 pointers -> start and end
    - maximze intial area
[1,7,2,5,4,7,3,6]
   | 
               |

how do we shift our pointers?
 - shift based on height
 - whichever is less, shift that one

running max

shift until collision
'''