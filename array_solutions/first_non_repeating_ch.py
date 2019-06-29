def first_non_repeating_ch(string):
    order=[]
    map={}
    for ch in string:
        if ch in map:
            ch[map]+=1
        else:
            ch[map]=1
            order.append(ch)
    for ch in order:
        if ch==1:
            return map[ch]
    return None