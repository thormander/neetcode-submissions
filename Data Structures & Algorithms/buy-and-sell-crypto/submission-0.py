class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        stack = []

        for price in prices:
            if not stack:
                stack.append(price)
                continue
            
            if price > stack[-1]:
                result = max(result,price - stack[-1])
            else:
                stack.pop()
                stack.append(price)
        
        return result


'''
running max = 6

[10,1,5,6,7,1]
              |

[1]
'''