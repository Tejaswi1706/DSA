class Solution(object):
    def twoSum(self, numbers, target):       
        i = 0
        j = len(numbers) - 1
        while(i < j):
            if(target < numbers[i] + numbers[j]):
                j -= 1
            elif(target > numbers[i] + numbers[j]):
                i += 1
            else:
                return [i, j]
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))  # LeetCode does this