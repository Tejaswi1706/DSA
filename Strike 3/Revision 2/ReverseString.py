s = ["h","e","l","l","o"]

first = 0
last = len(s) - 1

while first < last:
    tmp = s[last]
    s[last] = s[first]
    s[first] = tmp
    first += 1
    last -= 1
print(s)