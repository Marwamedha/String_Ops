def f(s):
    t = s[0]
    for i in range(len(s)-1):
        if(s[i+1] != s[0]):
            t += s[i+1]
        elif(s[i+1:i+len(t)+1] != t):
            t += s[i+1]
        else:
            break
    k=s.count(t)
 
    return (t, k)

def is_palindrome(s):
    s=s.lower()
    b=s[::-1]
    if s==b:
        return True
    else:
        return False


def solve (str1, str2): 
    locs = '' 
    k=str1.find('*')
    if str1 == str2:
        return True
    elif len(str1) > len(str2)and ('*' in str1):
        z=str1.replace('*','')
        print(z)
        if z == str2:
            return True
        else:
            return False
    elif (len(str1) <= len(str2) ) and ('*' in str1):
        for i in range(k, len(str2)): 
            locs+=str2[i]
            c=str1.replace('*',locs)
            if len(c) == len(str2) and c== str2 :
                return True
            elif len(c) == len(str2) and c!= str2 :
                return False
            else:
                c =''            
    else :
        return False