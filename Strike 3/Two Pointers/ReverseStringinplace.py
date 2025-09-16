s = ["h","e","l","l","o"]

first = 0
last = len(s) - 1
j = ''
k = ''

while first < last:
    j = s[first]
    k = s[last]
    s[first] = k
    s[last] = j
    first += 1
    last -= 1
print(s)
