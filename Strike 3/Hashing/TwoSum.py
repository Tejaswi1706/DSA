arr = [5, 2, 7, 10, 3, 9]

target = 8

hashmap = {}

for i in range(0, len(arr)):
    if target - arr[i] in hashmap:
        print(i, hashmap[target - arr[i]])
        break
    else:
        hashmap[arr[i]] = i