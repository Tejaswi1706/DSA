nums = [10,4,-8,7]

prefix_sum = []

prefix_sum.append(nums[0])

for i in range(1, len(nums)):
    prefix_sum.append(prefix_sum[i-1] + nums[i])

count = 0

for i in range(0, len(prefix_sum) - 1):
    if(prefix_sum[i] >= prefix_sum[len(nums)-1] - prefix_sum[i]):
        count += 1

