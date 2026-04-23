class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            # validate left
            while left <= right and s[left].isalnum() == False:
                left += 1

            # validate right
            while left <= right and s[right].isalnum() == False:
                right -= 1

            # compare
            if left <= right and s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True


        
'''
ignore case, and non alnum

isalnum()

two pointers
    one on each end
    increment them until they hit a valid char to compare

"tab a cat" 
     |
     |

'''