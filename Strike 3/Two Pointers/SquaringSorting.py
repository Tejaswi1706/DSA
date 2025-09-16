nums = [-4,-1,0,3,10]

for i in range(0, len(nums)):
    nums[i] = nums[i]**2

left = 0
right = 1
tmp = 0

while left < right:
    #print(nums[left], nums[right])
    if right < len(nums) and nums[left] >= nums[right]:
        print(left, right)
        tmp = nums[right]
        nums[right] = nums[left]
        nums[left] = tmp
        right += 1
    else:
        left += 1
        right = left + 1
        print(left, right)
        if left >len(nums) or right > len(nums):
            break
print(nums)

