s = 'ace'

t = 'abcde'

first = 0

second = 0

count = 0

while first < len(s) and second < len(t):
    if s[first] == t[second]:
        first += 1
        second += 1
        count += 1
    else:
        second += 1
if count == len(s):
    print('yes')
else:
    print('False')