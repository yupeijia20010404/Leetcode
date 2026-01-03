def isValid(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        char = s[i]
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if len(stack) == 0:
                return False
            else:
                previous = stack.pop()
                if char == ')' and previous != '(' :
                    return False
                elif char == '}' and previous != '{':
                    return False
                elif char == ']' and previous != '[':
                    return False
        else:
            return False
    return len(stack) == 0