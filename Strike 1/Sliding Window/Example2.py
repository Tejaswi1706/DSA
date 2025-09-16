s = "1101100111"

right = 0
left = 0
answer = 0
count = 0

for right in range (0, len(s)):

    if(s[right] == '0'):
        count += 1

    while(count > 1):
        left += 1
        if(s[left] == '0'):
            left += 1
            count -= 1
    
    if(count == 1):
        answer = max(answer, right - left + 1)
    print(left, right, count, answer)
print(answer)