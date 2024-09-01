# Note: Counter returns a dictionary of key-value pairs where keys represent the elements of the 
# array where as value represents the number of instances of that key inside that array.

from collections import Counter

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        for key,count in Counter(A).items():
            if count >=2:
                return key
        return -1