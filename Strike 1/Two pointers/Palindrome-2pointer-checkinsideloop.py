s = input()

i = 0
j = len(s) - 1

while(i <= j):
    if(s[i] == s[j]):
        if(i == j or i == j - 1):
            print("palindrime")
        i += 1
        j -= 1

    else:
        print("Not a palindrome")
        break

