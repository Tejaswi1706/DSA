nums = [1, 2, 4, 6, 8, 9, 14, 15]

target = 13

first = 0

last = len(nums) - 1

while first < last:
    if nums[first] + nums[last] > target:
        last -= 1
    elif nums[first] + nums[last] < target:
        first += 1
    elif nums[first] + nums[last] == target:
        print('True')
        break