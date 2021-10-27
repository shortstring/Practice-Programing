# 5. Longest Palindromic Substring
# Medium

# 13904

# 821

# Add to List

# Share
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return None
        current = s
        longest = ''       
        length = len(s)
        if length == 1:
            return s
        if length == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        used = {}
        #find first letter to repear
        for i in s:
            if i in used:
                used[i] += 1
            else:
                used[i] = 1
        for j in s:
            if used[j] ==

        print(used)

            
            
        
        return longest
        
def main():
    # print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
main()