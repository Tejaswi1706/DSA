arr = [1, 2, 4, 6, 8, 9, 14, 15]

n = 13

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] + arr[j] == n):
            print(arr[i], arr[j])
            break


