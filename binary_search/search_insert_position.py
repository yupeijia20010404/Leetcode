def searchInsert(nums, target):
    if target < nums[0]:
        return 0
    if target > nums[len(nums) - 1]:
        return len(nums)
    l = 0
    h = len(nums) - 1
    while l <= h:
        mid = (l + h) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        if nums[mid] > target:
            h = mid - 1
        if l == h:
            if nums[l] < target:
                return l + 1
            else:
                return l
        if l > h:
            return l