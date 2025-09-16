t = 'abcde'

s = 'ace'

first = 0
second = 0
count = 0

while second <= first and second < len(s) and first < len(t):
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
