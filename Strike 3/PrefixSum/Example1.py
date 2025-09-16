nums = [1, 6, 3, 2, 7, 2]

queries = [[0, 3], [2, 5], [2, 4]]

limit = 13

prefix = []

curr = 0

for i in range(0, len(nums)):
    curr += nums[i]
    prefix.append(curr)

prefixsum = 0   
result = []

for j in range(0, len(queries)):
    #print(queries[j][1])
    prefixsum = prefix[queries[j][1]] - prefix[queries[j][0]] + nums[queries[j][0]]
    #print(prefix[queries[j][1]], prefix[queries[j][0]], nums[queries[j][1]], prefixsum, result)
    if prefixsum < limit:
        result.append(True)
    else:
        result.append(False)
print(result)
