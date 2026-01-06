def mySqrt(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    l = 0
    r = x
    while l <= r:
        mid = (l + r) // 2
        if mid ** 2 <=x and (mid + 1) ** 2 > x:
            return mid
        if (mid + 1) ** 2 <= x:
            l = mid
        if mid ** 2 > x:
            r = mid