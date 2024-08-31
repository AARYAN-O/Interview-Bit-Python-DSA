class Solution:
	# @param A : integer
	# @return an integer
	def isPrime(self, A):
        if A<2:
            return 0
        sqrt_A=int(A**0.5)
        for i in range(2,sqrt_A+1):
            if i<A and A%i==0:
                return 0
        return 1

Note :

# 1) Time Complexity : O(sqrt(N))
# 2) roots and sqrts matter while calculating time complexities.
