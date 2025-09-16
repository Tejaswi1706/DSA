s = 'aceba'

first = 0

last = len(s) - 1

while first < last:
    if s[first] == s[last]:
        first += 1
        last -= 1
    else:
        break

if first >= last:
    print('True')
else:
    print('False')