def isSubsequence(s, t):
    if len(s) == 0:
        return True
    s_p = 0
    t_p = 0
    while t_p < len(t):
        if s[s_p] == t[t_p]:
            s_p += 1
        t_p += 1
        if s_p == len(s):
            return True
    return s_p == len(s)