class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
		if str(A)==str(A)[::-1] and A>=0:
			return 1
		return 0
