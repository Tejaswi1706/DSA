s = 'ace'

t = 'abcde'

first = 0

second = 0

while first < len(s) and second < len(t):
    if s[first] == t[second]:
        first += 1
        second += 1
    else:
        second += 1

if first == len(s):
    print('yes')
else:
    print('no')