nums = [-1,0]

target = -1

left = 0

right = len(nums) - 1

while left < right:
    if nums[left] + nums[right] > target:
        right -= 1
    elif nums[left] + nums[right] < target:
        left += 1
    if nums[left] + nums[right] == target:
        print([left + 1, right + 1])
        break

