s = 'abccbaacz'

seen = set()

for i in range(0, len(s)):
    if s[i] in seen:
        print(s[i])
        break
    else:
        seen.add(s[i])
