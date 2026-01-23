class Solution():
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def myPow(x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        i = 0
        result = 1.0
        if n >= 0:
            while(i < n):
                result = result * x
                i += 1
        else:
            while (i > n):
                result = result * (1/x)
                i -= 1
        return result
    
s = Solution
print(s.myPow(2, 0))
