class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = j = 0

        if(s == ''):
            return True
        elif(t == ''):
            return False

        while(i <= len(s) and j <= len(t)):
            if(j == len(t) - 1):
                if(i == len(s) - 1):
                    if(s[i] != t[j]):
                        return False
                        break
                    else:
                        return True
                        break
                if(i < len(s)):
                    return False
                    break
            elif(i < len(s) - 1 and j == len(t) - 1 and s[i] != t[j]):
                return False
                break
            elif(s[i] == t[j]):
                i += 1
                j+= 1
            else:
                j += 1

solution = Solution()
print(solution.isSubsequence("b", "abc"))  # LeetCode does this
print(solution.isSubsequence("axc", "ahbgdc"))
        

    

