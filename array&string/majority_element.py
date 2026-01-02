def majorityElement(nums):
    count = 0
    number = nums[0]
    for num in nums:
        if count == 0:
            number = num
        if num == number:
            count += 1
        else:
            count -= 1
    return number