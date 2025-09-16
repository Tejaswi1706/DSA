nums = [1,-2,-3]

prefix = []

curr = 0

for i in range(0, len(nums)):
    curr += nums[i]
    prefix.append(curr)

j = 1
count = 0



while j > 0 and count < len(prefix):
    for i in range(0, len(prefix)):
        #print(j, prefix[i])
        if j + prefix[i] >= 1:
            #print(j, prefix[i])
            count += 1
        else:
            j+= 1
            count = 0
            break

print(j)
    



        
