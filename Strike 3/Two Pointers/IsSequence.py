t = 'abcde'

s = 'abce'

first = 0

second = 0

count = 0

while second < len(s) and first < len(t):
    if s[second] != t[first]:
        first += 1
    else:
        first += 1
        second += 1
        count += 1

if count == len(s):
    print('yes')
else:
    print('false')


    #   i = j = 0

    #     if(s == ''):
    #         return True
    #     elif(t == ''):
    #         return False

    #     while(i < len(s) and j < len(t)):
    #         if(s[i] == t[j]):
    #             i += 1
    #             j += 1
    #         else:
    #             j += 1
        
    #     if(i == len(s) and s[i-1] == t[j-1]):
    #         return True
    #     else:
    #         return False

