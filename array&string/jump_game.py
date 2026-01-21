def canJump(nums):
    pos = len(nums) - 1
    while pos > 0 :
        current_pos = pos
        for i in range(pos - 1, -1, -1):
            if i + nums[i] >= current_pos:
                pos = i
        if pos == current_pos:
            return False
    return True