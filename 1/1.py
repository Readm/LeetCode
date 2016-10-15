class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        origin = list(nums)
        nums.sort()

        def find(lst, num):
            if len(lst) == 1:
                return num == lst[0]
            elif len(lst) == 0:
                return False
            else:
                if lst[len(lst) / 2] > num:
                    return find(lst[:len(lst) / 2], num)
                elif lst[len(lst) / 2] < num:
                    return find(lst[len(lst) / 2 + 1:], num)
                else:
                    return True

        for i in range(len(nums)):
            if find(nums[i + 1:], target - nums[i]):
                a = nums[i]
                index0 = origin.index(a)
                index1 = origin.index(target - a)
                if index0 == index1:
                    index1 = origin[index1 + 1:].index(target - a) + index1 + 1
                return [min(index0, index1), max(index0, index1)]

#89ms
a = Solution()
print a.twoSum([0, 4, 3, 0], 0)
