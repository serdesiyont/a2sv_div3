#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
   
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def sort_by_length(words):
            return len(words)
        output = ""
        strs.sort(key=sort_by_length)
        """
        sorted the string by length to iterate by the shortest string
        """

        for j in range(len(strs[0])):
            for s in strs:
                if s[j] != strs[0][j]:           
                    return output
                    
            output += strs[0][j]
        return output
        """compare each string with the first string at the same index
           if they aren't the same return output and break the loop,
           otherwise concatenate the characters to the output
        """   
    
    
# @lc code=end

