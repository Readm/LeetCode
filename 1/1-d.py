class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d.keys():
                return [d[target - nums[i]], i]
            else:
                d[nums[i]] = i


#645ms
a = Solution()
print a.twoSum([0, 4, 3, 0], 0)
