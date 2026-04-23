class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {")":"(" , "}":"{" , "]":"["}

        for char in s:
    
            if char not in pairs:
                # append any openers
                stack.append(char)
            else:
                # case of closer
                if not stack or pairs[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if not stack:
            return True
        else:
            return False
            

'''
stack
[]

add open brackets to stack
if we come across a closing:
    check top of stack to see if it closes --> pop if it does, reutrn false if not

if its empty return true
'''