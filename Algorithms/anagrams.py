def Anagrams(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2


s1 = "abba"
s2 = "baba"
print("true" if Anagrams(s1, s2) else "false")
