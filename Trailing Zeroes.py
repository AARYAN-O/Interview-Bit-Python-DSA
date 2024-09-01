# here I have taken advantage of the fact that the binary numbers can consist of only 0s and 1s.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        x=str(bin(A))
        lst=x.split('1')
        return len(lst[-1])
        
