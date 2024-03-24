class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
        return prefix