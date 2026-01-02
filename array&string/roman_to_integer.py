def romanToInt(self, s: str) -> int:
    pointer = 0
    number = 0
    while pointer < len(s):
        if s[pointer] == 'C':
            if pointer != len(s) -  1 and s[pointer + 1] == 'M':
                number += 900
                pointer += 2
            elif pointer != len(s) -  1 and s[pointer + 1] == 'D':
                number += 400
                pointer += 2
            else:
                number += 100
                pointer += 1
        elif s[pointer] == 'X':
            if pointer != len(s) -  1 and s[pointer + 1] == 'L':
                number += 40
                pointer += 2
            elif pointer != len(s) -  1 and s[pointer + 1] == 'C':
                number += 90
                pointer += 2
            else:
                number += 10
                pointer += 1
        elif s[pointer] == 'I':
            if pointer != len(s) -  1 and s[pointer + 1] == 'V':
                number += 4
                pointer += 2
            elif pointer != len(s) -  1 and s[pointer + 1] == 'X':
                number += 9
                pointer += 2
            else:
                number += 1
                pointer += 1
        else:
            if s[pointer] == 'V':
                number += 5
            elif s[pointer] == 'L':
                number += 50
            elif s[pointer] == 'D':
                number += 500
            elif s[pointer] == 'M':
                number += 1000
            pointer += 1
    return number
                