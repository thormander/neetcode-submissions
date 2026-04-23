class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # handle carryover
        # iterate backwards, and if its 9 just set to 0 and carry over 1
        # if we have a leading 0, just insert a 1 at the front.

        right = len(digits) - 1

        while right > -1:
            
            if digits[right] != 9:
                digits[right] += 1
                return digits
            else:
                digits[right] = 0 # case of 9

            right -= 1
        
        # if we get through this without returning, means we had all 9's
        digits.insert(0,1)
        return digits

        