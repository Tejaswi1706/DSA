arr = [1,1,3,3,5,5,7,7]

count = 0

for i in range(0, len(arr)):
    if arr[i] + 1 in arr:
        count += 1

print(count)