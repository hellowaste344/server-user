class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #range(start, stop, step)
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits #ends the loop as it returns 
            digits[i] = 0 #works if condition isn't satisfied

        return [1] + digits #[1] + [*digits]
