class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(s)
        integer = 0
        for i in range(len(s_list)):
            if s_list[i] == 'I':
                if i < len(s_list) - 1 and s_list[i + 1] == 'V':
                    integer += 4
                elif i < len(s_list) - 1 and s_list[i + 1] == 'X':
                    integer += 9
                else:
                    integer += 1
            elif s_list[i] == 'X':
                if i > 0 and s_list[i - 1] == 'I':
                    continue
                if i < len(s_list) - 1 and s_list[i + 1] == 'L':
                    integer += 40
                elif i < len(s_list) - 1 and s_list[i + 1] == 'C':
                    integer += 90
                else:
                    integer += 10
            elif s_list[i] == 'C':
                if i > 0 and s_list[i - 1] == 'X':
                    continue
                if i < len(s_list) - 1 and s_list[i + 1] == 'D':
                    integer += 400
                elif i < len(s_list) - 1 and s_list[i + 1] == 'M':
                    integer += 900
                else:
                    integer += 100
            elif s_list[i] == 'V':
                if i > 0 and s_list[i - 1] == 'I':
                    continue
                integer += 5
            elif s_list[i] == 'L':
                if i > 0 and s_list[i - 1] == 'X':
                    continue
                integer += 50
            elif s_list[i] == 'D':
                if i > 0 and s_list[i - 1] == 'C':
                    continue
                integer += 500
            elif s_list[i] == 'M':
                if i > 0 and s_list[i - 1] == 'C':
                    continue
                integer += 1000
        return integer