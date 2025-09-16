arr = [1, 2, 4, 6, 8, 9, 14, 15]

n = 13

i = 0
j = len(arr) - 1

while(i < j):
    if(arr[i] + arr[j] > n):
        j -= 1
    elif(arr[i] + arr[j] < n):
        i += 1
    else:
        print(arr[i], arr[j])
        break
