arr2 = [1, 4, 7, 20]
arr1 = [3, 5, 6]
arr3 = []

i = j = 0

while(len(arr3) != len(arr1) + len(arr2)):
    if(i >= len(arr1)):
        arr3.append(arr2[j])
        j += 1
    elif(j >= len(arr2)):
        arr3.append(arr1[i])
        i += 1
    elif(i < len(arr1)):
        if(arr1[i] < arr2[j]):
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    elif(j < len(arr2)):
        if(arr1[i] > arr2[j]):
            arr3.append(arr2[j])
            j += 1
        else:
            arr3.append(arr1[i])
            i += 1


print(arr3)


