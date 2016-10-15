class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=set([])
        for i in range(len(nums)):
            if target-nums[i] in s:
                return [nums[:i].index(target-nums[i]), i]
            else:
                s.add(nums[i])


#59ms
a = Solution()
print a.twoSum([0, 4, 3, 0], 0)
