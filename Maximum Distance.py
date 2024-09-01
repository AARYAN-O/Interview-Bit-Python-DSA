# In this method , the time limit gets exceeded.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        lst=[]
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i]<=A[j]:
                    lst.append(j-i)
        return max(lst)

