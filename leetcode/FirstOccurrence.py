class Solution(object):
    def strStr(self, haystack, needle):
        
        # return haystack.find(needle) .find(sub, start, end)
        
        # return haystack.index(needle) if needle in haystack else -1
           
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
