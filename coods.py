def is_palindrome(s):
    try:
        s=s.lower()
        b=s[::-1]
        if s==b:
            return True
        else:
            return False
    except:
        print("wrong input.")
        
        

def solve (str1, str2):
    try:
        if (str1 == str2):
            return True

        elif("*" in str1):
            astric_loc = str1.find('*')
            new_str = str1.replace("*", str2[astric_loc:astric_loc+1+(len(str2)-len(str1))])
            return new_str == str2
        else:
            return False
    except:
        print("Wrong input!")
        
        
def f(s):
    try:
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
    except:
        print("wrong input")
        
        
        
def find_nth_occurrence(substring, string, occurrence=1):
    try:
        loc = 0
        for i in range(occurrence):
            loc = string.find(substring, loc)
            loc += 1

        return loc - 1
    except:
        print("Wrong input!")
