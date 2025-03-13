def longest(arr):
    st = set()
    res = 0
    
    for val in arr:
        st.add(val)
    
    for val in arr:
        if val in st and (val - 1) not in st:
            cur = val
            cnt = 0
            while cur in st:
                st.remove(cur)
                cur +=1
                cnt +=1
            res = max(res, cnt)
    return res
        

arr = [2, 6, 6, 1, 9, 4, 5, 3]
longest(arr)