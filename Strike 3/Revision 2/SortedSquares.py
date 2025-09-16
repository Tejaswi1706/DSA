nums = [-4,-1,0,3,10]

sorted = [0]*len(nums)

first = 0
last = len(nums) - 1
index = len(nums) - 1
tmp = 0

while first < last:
    if nums[first] * nums[first] > nums[last] * nums[last]:
        sorted[index] = nums[first] * nums[first]
        index -= 1
        first += 1
    else:
        sorted[index] = nums[last] * nums[last]
        index -= 1
        last -= 1
