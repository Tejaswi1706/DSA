nums = [1, 2, 4, 6, 8, 9, 14, 15]

target = 13

left = 0
right = len(nums) - 1

while left < right:
    if nums[left] + nums[right] == target:
        print('True')
        break
    else:
        left += 1
        right -= 1
if left >= right:
    print('False')