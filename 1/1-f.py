class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            try:
                return [d[target - nums[i]], i]
            except:
                d[nums[i]] = i


#62ms
a = Solution()
print a.twoSum([0, 4, 3, 0], 0)
