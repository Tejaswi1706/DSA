class Solution(object):
    def isSubsequence(self, s, t):
        i = j = 0

        if(s == ''):
            return True
        elif(t == ''):
            return False

        while(i < len(s) and j < len(t)):
            if(s[i] == t[j]):
                i += 1
                j += 1
            else:
                j += 1
        
        if(i == len(s) and s[i-1] == t[j-1]):
            return True
        else:
            return False
        
solution = Solution()
print(solution.isSubsequence("acb", "ahbgdc"))  # LeetCode does this
print(solution.isSubsequence("axc", "ahbgdc"))