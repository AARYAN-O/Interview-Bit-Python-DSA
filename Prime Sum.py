# The method below fails because it has time complexity of O(N square) and gives TLE.

class Solution:
	# @param A : integer
	# @return a list of integers
    def sieve(self,A):
        is_prime=[True]*(A+1)
        is_prime[0]=is_prime[1]=False
        for p in range(2,int(A**0.5)+1):
            for multiple in range(p*p,A+1,p):
                is_prime[multiple]=False
        return ([index for index,value in enumerate(is_prime) if value==True])

        
	def primesum(self, A):
        lst=[]
        primes=self.sieve(A)
        for i in primes:
            for j in primes:
                if i+j==A:
                    lst.append([i,j])
        return sorted(lst)[0]


# The second method also fails because of TLE:

class Solution:
	# @param A : integer
	# @return a list of integers
    def sieve(self,A):
        is_prime=[True]*(A+1)
        is_prime[0]=is_prime[1]=False
        for p in range(2,int(A**0.5)+1):
            for multiple in range(p*p,A+1,p):
                is_prime[multiple]=False
        return ([index for index,value in enumerate(is_prime) if value==True])

        
	def primesum(self, A):
        lst=[]
        primes=self.sieve(A)
        # return primes
        for i in primes:
            if i and (A-i in primes):
                return [i,A-i]

# Best time complexity : O(N)

class Solution:
	# @param A : integer
	# @return a list of integers
    def is_prime(self,n):
        if n<2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
        
        
	def primesum(self, A):
        for i in range(2,A):
            if self.is_prime(i) and self.is_prime(A-i):
                return [i,A-i]
                