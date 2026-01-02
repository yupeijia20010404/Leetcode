def isIsomorphic(s, t):
    explored = set()
    mapping = dict()
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if not s[i] in mapping and not t[i] in explored:
            mapping[s[i]] = t[i]
            explored.add(t[i])
        else:
            if (s[i] not in mapping and t[i] in explored) or (s[i] in mapping and t[i] not in explored):
                return False
            if mapping[s[i]] != t[i]:
                return False
    return True

print(isIsomorphic('paper', 'title'))