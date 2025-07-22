
print("----head Recursion------")
def fun(x,n):
    if(n==0):
        return
    print(f"{x} {n}")
    fun(x,n-1)
fun(15,5)

print("----Tail Recursion------")
def fun2(x,n):
    if(n==0):
        return
    fun2(x,n-1)
    print(f"{x} {n}")
fun2(15,5)