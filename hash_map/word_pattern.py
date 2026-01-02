def wordPattern(pattern, s):
    explored = set()
    mapping = dict()
    s_word = s.split()
    if len(pattern) != len(s_word):
        return False
    for i in range(len(pattern)):
        if not pattern[i] in mapping and not s_word[i] in explored:
            mapping[pattern[i]] = s_word[i]
            explored.add(s_word[i])
        else:
            if (pattern[i] not in mapping and s_word[i] in explored) or \
            (pattern[i] in mapping and s_word[i] not in explored):
                return False
            if mapping[pattern[i]] != s_word[i]:
                return False
    return True