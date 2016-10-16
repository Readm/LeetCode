class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        m = 0
        left = 0
        d = { }

        for i in range(len(s)):
            last = d.get(s[i], None)
            if last:
                left = max(left, last)
                #left = last if last > left else left      #same
            if i-left+1 > m:
                m = i-left+1
            d[s[i]] = i+1
        return m


# 92ms
a = Solution()
print a.lengthOfLongestSubstring("abcabc")