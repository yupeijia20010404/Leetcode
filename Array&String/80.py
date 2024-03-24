class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = nums[0]
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[i - 1] or (nums[i] == nums[i - 1] and nums[i] != p):
                p = nums[k - 1]
                nums[k] = nums[i]
                k += 1
        return k