def isPalindrome(s):
    l = 0
    r = len(s) - 1
    while l <= r:
        while not (s[l].isalpha() or s[l].isdigit()):
            l += 1
            if l > r:
                return True
        while not (s[r].isalpha() or s[r].isdigit()):
            r -= 1
            if l > r:
                return True
        if s[l].isalpha() and s[r].isalpha():
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        elif s[l].isdigit() and s[r].isdigit():
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        else:
            return False
    return True

isPalindrome('A man, a plan, a canal: Panama')