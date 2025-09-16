nums = [1, 6, 3, 2, 7, 2]

queries = [[0, 3], [2, 5], [2, 4]]

limit = 13

prefix_sum = [nums[0]]

for i in range(1, len(nums)):
    prefix_sum.append(prefix_sum[i-1] + nums[i])

query = []

for j in queries:
    if (prefix_sum[j[1]] - prefix_sum[j[0]] + nums[j[0]]) < limit:
        query.append(True)
    else:
        query.append(False)

print(query)


