def containsNearbyDuplicate(nums, k):
    index = {}
    for i in range(len(nums)):
        if nums[i] in index and abs(index[nums[i]] - i) <= k:
            return True
        else:
            index[nums[i]] = i
    return False