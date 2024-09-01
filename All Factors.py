# Given a number A, find all factors of A.

# O(N/2)= O(N) --> time complexity , but we are getting   TLE 

class Solution:
	# @param A : integer
	# @return a list of integers
	def allFactors(self, A):
        lst=[]
        for i in range(1,A//2+1):
            if A%i==0 :
                lst.append(i)
        lst.append(A)
        return lst

# O(SQRT(N)) --> time complexity reduced

class Solution:
	# @param A : integer
	# @return a list of integers
	def allFactors(self, A):
        st=set()
        for i in range(1,int(A**0.5)+1):
            if A%i==0:
                st.add(i)
                st.add(A//i)
        return sorted(st)