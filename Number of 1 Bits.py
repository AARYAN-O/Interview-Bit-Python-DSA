class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        lst=[]
        x=str(bin(A))
        for i in x[2:]:
            if i=='1':
                lst.append(i)
        return len(lst)
