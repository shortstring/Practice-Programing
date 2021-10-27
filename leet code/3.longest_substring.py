class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        seen  = ''
        for letter in s:
            if letter not in seen:
                seen += letter
            else:
                seen = seen[seen.index(letter) + 1:] + letter
            longest = max(longest, len(seen))
        return longest
def main():
    my_solution = Solution()
    print(my_solution.lengthOfLongestSubstring("abcabcbb"))

main()