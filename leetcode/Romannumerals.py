class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    R = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }        
    result = 0
    for n in range(len(s)):
        if R.get(s[n]) < R.get(s[n+1]):
            result -= R.get(s[n]) 
        else: 
            result += R.get(s[n])