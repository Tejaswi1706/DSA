nums = [1,2,3,4,5]

k = 1

right = 0
left = 0
curr = 1
answer = 0

for right in range(0, len(nums)):
    curr *= nums[right]

    while(curr >= k and left < len(nums)):
        curr /= nums[left]
        left += 1
    print(curr, right, left) 

    if(curr < k):
        answer += right - left + 1
    print(answer)


print(max(0, answer))