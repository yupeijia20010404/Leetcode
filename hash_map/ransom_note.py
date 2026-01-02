def canConstruct(ransomNote, magazine):
    magazine_list = list(magazine)
    for char in ransomNote:
        if char in magazine_list:
            magazine_list.remove(char)
        else:
            return False
    return True