
def fact(n):
    if n<1 and n==0:
        return 1
    return n*(fact(n-1))
data = fact(4)
print(data)