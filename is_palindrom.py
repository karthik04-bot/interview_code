def is_palindrome(s):
    i=0
    j=len(s)-1
    s=s.strip()
    while i<j:
       if s[i].lower()==s[j].lower():
           i+=1
           j-=1
       else:
           return False
    return True

s=["A man, a plan, a canal: Panama","race a car"]
for i in s:
    print(i)
    b=is_palindrome(i)
    if b:
        print("Its a palindrome")
    else:
        print("Its not palindrome")
