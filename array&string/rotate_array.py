class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        step = k % len(nums)
        front = nums[len(nums) - step : len(nums)]
        behind = nums[: len(nums) -  step]
        nums[: step] = front
        nums[step: ] = behind