def isHappy(n):
    explored = set()
    if n < 4 and n != 1:
        return False
    while n >= 4:
        result = 0
        digits = list(str(n))
        n = sum([int(d) ** 2 for d in digits])
        if n in explored:
            return False
        if n < 4 and n != 1:
            return False
        explored.add(n)
    return True

isHappy(4)