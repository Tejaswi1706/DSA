s = 'aceba'

left = 0

right = len(s) - 1

while left <= right:
    if s[left] == s[right]:
        left += 1
        right -= 1
    else:
        print('No')
        break
if(left >= right):
    print('yes')