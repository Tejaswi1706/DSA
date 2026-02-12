class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 1
        while(i < len(nums)):
            if(target == nums[i] + nums[j]):
                return i, j
            elif(target != nums[i] + nums[j]):
                j += 1
                if(j == len(nums)):
                    i += 1
                    j = i + 1
            else:
                i += 1
solution = Solution()
print(solution.twoSum([3,3], 6))  # LeetCode does this