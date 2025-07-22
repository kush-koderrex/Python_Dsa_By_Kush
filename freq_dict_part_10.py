# Store Frequency In Dictonary
num = [5,6,7,7,1,9,111,1,1,5,1,1]
freq_heap = {}
for i in range(0,len(num)):
    if num[i] in freq_heap:
        freq_heap[num[i]] +=1 
    else:
        freq_heap[num[i]]=1
print(freq_heap)
