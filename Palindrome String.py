# There is no such concept of directly converting the strings into a string where al num charactes 
# are replaced.

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        s=''
        for character in A:
            if character.isalnum():
                s=s+character
        if s[::].lower()==s[::-1].lower():
            return 1
        return 0
                