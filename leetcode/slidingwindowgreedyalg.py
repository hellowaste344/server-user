class Solution:
    def subarraySum(self, arr, target):
        # code here
        l = 0
        current_sum = 0
        
        for r in range(len(arr)):
            current_sum += arr[r]
            
            while current_sum > target and l <= r:
                current_sum -= arr[l]
                l += 1
                
            if current_sum == target:
                return [l+1, r+1]
        
        return [-1]
    
arr = [16,13,24,32,21,48,4,9]
target = 9

s = Solution()
print(s.subarraySum(arr, target))