class Solution:
	# @param A : integer
	# @return an integer
	def reverse(self, A):
		if A>0:
			rev_int=int(str(A)[::-1])
			if rev_int > 2**31-1 or rev_int < - 2**31:
				return 0
			return rev_int
		else:
			rev_int= - int(str(A)[-1:0:-1])
			if rev_int > 2**31-1 or rev_int < - 2**31:
				return 0
			return rev_int
