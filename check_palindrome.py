s = "nitin"
t = "mom"
d = "kush"

# def checkPalin (s):
#     if (s[::-1]==s):
#         print("Yes Its an Palindrome")
#     else:
#         print("Not a Palindrome")
# checkPalin(d)

# check palindrome using recurion

def checkPalinUsingRecurion(s,l,r):
    if l>=r:
        print("palindrome")
        return
    else:
        print("Not a palindrome")
        return
    checkPalinUsingRecurion(s,l+1,r-1)
  
checkPalinUsingRecurion(s,0,len(s)-1)



# def checkPalinUsingRecursion(s, l, r):
#     if l >= r:
#         print("Palindrome")
#         return

#     if s[l] != s[r]:
#         print("Not a palindrome")
#         return

#     checkPalinUsingRecursion(s, l + 1, r - 1)

# # Example usage:
# s = "madam"
# checkPalinUsingRecursion(s, 0, len(s) - 1)