def twoSum1(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def twoSum2(nums, target):
    number_index = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in number_index:
            return number_index[complement]
        number_index[complement] = i