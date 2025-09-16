s = ["h","e","l","l","o"]

tmp = ''


first = 0
last = len(s) - 1

while first < last:
    tmp = s[first]
    s[first] = s[last]
    s[last] = tmp
    first += 1
    last -= 1

print(s)