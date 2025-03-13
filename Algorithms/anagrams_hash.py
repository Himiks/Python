def Anagrams(s1, s2):
    charCount = {}
    for ch in s1:
        charCount[ch] = charCount.get(ch, 0) + 1
    print(charCount)

    print("")
    
    for ch in s2:
        charCount[ch] = charCount.get(ch, 0) - 1
    print(charCount)    
    
    for value in charCount.values():
        if value != 0:
            return False
    return True

s1 = "abba"
s2 = "baba"
print("true" if Anagrams(s1, s2) else "false")