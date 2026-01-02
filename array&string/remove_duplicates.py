def removeDuplicates(nums):
    count = 0
    for i in range(1, len(nums)):
        pointer = i
        if count + pointer >= len(nums):
            break
        while nums[pointer] == nums[pointer - 1]:
            val = nums[pointer]
            nums[pointer : len(nums) - 1] = nums[pointer + 1 : len(nums)]
            nums[len(nums) - 1] = val
            count += 1
            if count + pointer >= len(nums):
                break
    return len(nums) - count