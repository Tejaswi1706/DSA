arr1 = [1, 4, 7, 20]

arr2 = [3, 5, 6]

first = 0

second = 0

arr3 = []

while first < len(arr1) and second < len(arr2):
    if arr1[first] < arr2[second]:
        arr3.append(arr1[first])
        first += 1
    else:
        arr3.append(arr2[second])
        second += 1

while first < len(arr1):
    arr3.append(arr1[first])
    first += 1
while second < len(arr2):
    arr3.append(arr2[second])
    second += 1

print(arr3)