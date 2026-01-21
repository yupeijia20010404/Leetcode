class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        duplicate = 0
        num = nums[0]
        count = 0
        i = 0
        swapped = 0
        while i < len(nums):
            while duplicate < 2 and i < len(nums) and nums[i] == num:
                duplicate += 1
                i += 1
            count += duplicate
            if i >= len(nums):
                return count
            if nums[i] == num:
                while nums[i] == num:
                    nums[count : len(nums) - 1] = nums[count + 1 : len(nums)]
                    nums[len(nums) - 1] = num
                    swapped += 1
                    if swapped + count == len(nums):
                        return count
            duplicate = 0
            num = nums[i]
            if swapped + count == len(nums):
                break
        return count