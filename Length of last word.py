class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
        A=A.strip(' ')
        lst=A.split(' ')
        return len(lst[-1])
