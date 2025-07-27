def fun(sum,i,n):
    if (i>n):
        print(sum)
        return
    fun(sum+i,i+1,n)
fun(0,1,4)


# Functional Recursion

def func(n):
    if (n==1):
        return 1
    return n+func(n-1)
a = func(10)
print(a)