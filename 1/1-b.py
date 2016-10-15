class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst=[]
        for i in range(len(nums)):
            if target-nums[i] in nums[:i]:
                return [nums[:i].index(target-nums[i]), i]

#542ms
#686ms
a = Solution()
print a.twoSum([0, 4, 3, 0], 0)
