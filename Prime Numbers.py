# Note: In sieve of erathosthenes method , we directly say that the multiples of prime numbers
# are not primes
# In this method , we do not find which number is prime and which is not.

class Solution:
	# @param A : integer
	# @return a list of integers
	def sieve(self, A):
		is_prime=[True]*(A+1)
		is_prime[0]=is_prime[1]=False
		for p in range(2,int(A**0.5)+1):
			if is_prime[p]:
				for multiple in range(p*p,A+1,p):
					is_prime[multiple]=False
		return [index+1 for index,value in enumerate(is_prime[1:]) if value==True]