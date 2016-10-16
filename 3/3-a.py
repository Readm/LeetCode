class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        def longest(index):
            _s = set()
            p = index
            while p < len(s):
                if s[p] in _s:
                    return p - index
                _s.add(s[p])
                p += 1
            return p - index

        return max([longest(i) for i in range(len(s))])


# time out
a = Solution()
print a.lengthOfLongestSubstring("c")
