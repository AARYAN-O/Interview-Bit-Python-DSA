# For rotating the array by n positions  , we need to make the use of 
# modulo operations.


# left rotation
class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        i=b%len(a)
        return a[i:] + a[:i]

# right rotation

class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        i=b%len(a)
        return a[-i:] + a[:-i]