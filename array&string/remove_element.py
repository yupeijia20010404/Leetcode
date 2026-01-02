def removeElement(nums, val):
    count = 0
    for i in range(0, len(nums)):
        pointer = i
        if count + i >= len(nums):
            break
        while nums[pointer] == val:
            nums[pointer : len(nums) - 1] = nums[pointer + 1 : len(nums)]
            nums[len(nums) - 1] = val
            count += 1
            if count + i >= len(nums):
                break
    return len(nums) - count

removeElement([4, 5], 4)
            