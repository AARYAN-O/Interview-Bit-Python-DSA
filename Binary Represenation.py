# Given a number N >= 0, find its representation in binary.

# Example:

# if N = 6,

# binary form = 110

class Solution:
	# @param A : integer
	# @return a strings
	def findDigitsInBinary(self, A):
        return str(bin(A))[2:]