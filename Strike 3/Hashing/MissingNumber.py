nums = [9,6,4,2,3,5,7,0,1]

numbers = set()

for i in range(0, len(nums) + 1):
    if i in nums:
        numbers.add(i)
    else:
        print(i)


