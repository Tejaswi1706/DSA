s = 'aceba'

left = 0
right = len(s) - 1

while left < right:
    if s[left] == s[right]:
        left += 1
        right -= 1
    else:
        print('no')
        break
if left >= right and s[left] == s[right]:
    print('yes')