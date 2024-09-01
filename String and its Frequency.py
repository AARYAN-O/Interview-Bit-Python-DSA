from collections import Counter
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        x=''
        for key,count in Counter(A).items():
            x=x+str(key)+str(count)
        return x