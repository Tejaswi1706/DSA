nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

right = 0
left = 0
curr = 0
answer = 0

for right in range(0, len(nums)):
    curr += nums[right]

    while(curr > k):
        curr -= nums[left]
        left += 1

    if(curr == k):
        answer = max(answer, right - left + 1)

    #right += 1

print(answer)
