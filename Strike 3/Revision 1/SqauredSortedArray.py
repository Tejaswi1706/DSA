nums = [-4, -1, 0, 3, 10]

for i in range(0, len(nums)):
    nums[i] = nums[i]**2

sortedarray = [0]*5

first = 0
last = len(nums) - 1
tmp = 0

while first < last:
    if nums[first] < nums[last]:
        if(sortedarray[last] < nums[last]):
            tmp = sortedarray[last]
            sortedarray[last] = nums[last]
        last -= 1
    else:
        if(sortedarray[first] > nums[first]):
            tmp = sortedarray[first]
            sortedarray[first] = nums[first]
        first += 1


    
print(sortedarray)



