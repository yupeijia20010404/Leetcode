def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = ''
    for i in range(len(strs[0])):
        for j in range(len(strs)):
            if i >= len(strs[j]):
                return prefix
            if strs[j][i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return prefix