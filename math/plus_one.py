def plusOne(digits):
    res = []
    carry = 0
    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]
        if i == len(digits) - 1:
            num = digit + carry + 1
        else:
            num = digit + carry
        if num >= 10:
            res.append(num % 10)
            carry = num // 10
        else:
            res.append(num % 10)
            carry = 0
    if carry > 0:
        res.append(carry)
    res.reverse()
    return res

print(plusOne([8, 9, 9, 9]))