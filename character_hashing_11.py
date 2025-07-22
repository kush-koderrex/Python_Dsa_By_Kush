s = "azyxyyzaaaa"
q=["d","a","y","x"]
hashlist = [0] * 27  
for fr in s:
    asi_val=ord(fr)
    index = asi_val - 97
    hashlist[index]+=1
print(hashlist)

for ch in q:
    asi_val=ord(ch)
    index = asi_val - 97
    print(f"{ch} {hashlist[index]}")
