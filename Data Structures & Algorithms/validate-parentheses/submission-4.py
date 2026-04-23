class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")" : "(","}" : "{", "]" : "["} # key: close | value: open

        stack = []

        for char in s:
            if char not in pairs:
                # must be open
                stack.append(char)
            else:
                # must be closed
                if stack and pairs[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False
        
'''
see if s is valid

brackets MUST be closed to be considered valid

also have a map so we know what goes to what
    - closing : open

stack

as we iterate
    - add any open paranethiese
    - as we run into closed paraenthesis, check top of stack to see if it closes it.
        if not return false
        if it does, pop top of stack

not actually adding any 'closing' side of the brackets
'''