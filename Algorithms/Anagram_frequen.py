MAX = 26


def Anagram(s1, s2):
    freq = [0] * MAX

    for ch in s1:
        freq[ord(ch) - ord("a")] += 1

    for ch in s2:
        freq[ord(ch) - ord("a")] -= 1

    for count in freq:
        if count != 0:
            return False
    return True


s1 = "abba"
s2 = "baba"
print("true" if Anagram(s1, s2) else "false")
