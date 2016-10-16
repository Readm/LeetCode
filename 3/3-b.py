class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max = 0
        left = 0

        for i in range(len(s)):
            if s[i] in s[left:i]:
                left += s[left:i].index(s[i])+1
            if i-left+1 > max:
                max = i-left+1
        return max


# 112ms
a = Solution()
print a.lengthOfLongestSubstring("")