num=[5,7,3,2,6,1,5,9]
left = 2
right = 5

# Buildin methord 
# num.reverse()
# # print(num)

# num[::-1]
# print(num)

# reverse an array Through Recursion
def func(num,l,r):
    if(l>=r):
        return
    num[l],num[r] = num[r],num[l]
    func(num,l+1,r-1)

func(num,left,right)
print(num)



        
