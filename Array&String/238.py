class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right_mul = 1
        left_mul = 1
        right = []
        left = []
        right.append(right_mul)
        left.append(left_mul)
        for i in range(1, len(nums)):
            left_mul *= nums[i - 1]
            left.append(left_mul)
        for i in range(len(nums) - 2, -1, -1):
            right_mul *= nums[i + 1]
            right.append(right_mul)
        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[len(nums) - i - 1])
        return result