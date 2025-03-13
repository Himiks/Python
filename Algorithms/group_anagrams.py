Max = 26

def getHash(s):
    hashList = []
    freq = [0] * Max

    for ch in s:
        freq[ord(ch) - ord("a")] += 1

    for i in range(Max):
        hashList.append(str(freq[i]))
        hashList.append("$")
    print("HashList:", hashList)

    return "".join(hashList)


def anagrams(arr):
    res = []
    mp = {}

    for i in range(len(arr)):
        key = getHash(arr[i])

        if key not in mp:
            mp[key] = len(res)
            res.append([])

        res[mp[key]].append(arr[i])

        print("Res:", res)
        print("Mp:", mp)

    return res


arr = ["act", "god", "cat", "dog", "tac"]
res = anagrams(arr)
for group in res:
    for word in group:
        print(word, end=" ")
    print()
