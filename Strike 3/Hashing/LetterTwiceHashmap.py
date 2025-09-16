s = 'abccbaacz'

h = {}

for i in range(0, len(s)):
    if s[i] in h:
        print(s[i])
        break
    else:
        h[s[i]] = i
        print(h)
