nums = [10, 4, -8, 7]

prefixsum = []

curr = 0

count = 0

for i in range(0, len(nums)):
    curr += nums[i]
    prefixsum.append(curr)

for j in range(0, len(prefixsum)-1):
    subsum = prefixsum[len(prefixsum)-1] - prefixsum[j]
    #print(prefixsum[j], subsum)
    if prefixsum[j] >= subsum:
        count += 1
print(count)