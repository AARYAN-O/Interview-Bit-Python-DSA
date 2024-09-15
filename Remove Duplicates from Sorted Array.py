class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        b=set(A)
        c=list(b)
        c.sort()
        for i in range(len(c)):
            A[i]=c[i]
        return len(c)
