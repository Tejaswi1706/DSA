nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]

k = 2

# left = 0
# right = 1
# sum = 0
# answer = 0

# for right in range(1, len(nums)):
#     sum = nums[left] + nums[right]

#     answer = max(answer, sum)
#     left += 1

# print(answer)

def find_best_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    
    return ans

print(find_best_subarray(nums, k))