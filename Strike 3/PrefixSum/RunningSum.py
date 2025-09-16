nums = [1,2,3,4]

sum = []

curr = 0

for i in range(0, len(nums)):
    curr += nums[i]
    sum.append(curr)

print(sum)