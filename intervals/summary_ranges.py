def summaryRanges(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [str(nums[0])]
    p = 1
    result = []
    start = nums[0]
    while p < len(nums):
        while p < len(nums) and nums[p] == nums[p - 1] + 1:
            p += 1
            continue
        if start == nums[p - 1]:
            result.append(str(start))
        else:
            result.append(str(start) + '->' + str(nums[p - 1]))
        if p == len(nums) - 1:
            result.append(str(nums[p]))
        elif p == len(nums):
            break
        else:
            start = nums[p]
        p += 1
    return result

nums = [0,2,3,4,6,8,9]
print(summaryRanges(nums))