s = input()

def checkpalindrome(s):

    i = 0
    j = len(s) - 1

    while(i < j):
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True

if(checkpalindrome(s) == True):
    print('palindrome')
else:
    print('not a palindrome')