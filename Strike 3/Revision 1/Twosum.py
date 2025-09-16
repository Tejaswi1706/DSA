nums = [2,7,11,15]

target = 9

left = 0
right = len(nums) - 1
count = 0

while left < right:
    if nums[left] + nums[right] > target:
        right -= 1
    elif nums[left] + nums[right] < target:
        left += 1
    else:
        count += 1
        print('True')
        break

if count != 1:
    print('False')
