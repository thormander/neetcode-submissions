class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left <= right:
            # make left valid
            while left <= right and (not s[left].isalnum()):
                left += 1

            # make right valid
            while left <= right and (not s[right].isalnum()):
                right -= 1
        
            # do the compare
            if left <= right and s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

'''
2 pointers
start, end

go through until they collide
    - if current char NOT alphanum, increment/decrement until it is

if at any point we find a diff, return false

after colliding
return true

"Was it a car or a cat I saw?"
 |       
                           |
 
'''