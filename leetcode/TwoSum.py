class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(0, len(nums)):
            value = nums[i]
            different = target - value
            # [1,3,4,5] target = 7 
            if value not in d:
                d[different]=i
            else:
                current_value = i
                previous_value = d[value]
                return [ current_value, previous_value ]