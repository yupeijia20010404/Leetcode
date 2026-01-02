def isAnagram(s, t):
    def get_count(string):
        count = dict()
        for char in string:
            count[char] = count.get(char, 0) + 1
        return count

    s_count = get_count(s)
    t_count = get_count(t)
    if len(s_count.keys()) != len(t_count.keys()):
        return False
    for k, v in s_count.items():
        if k not in t_count or t_count[k] != v:
            return False
    
    return True
    
