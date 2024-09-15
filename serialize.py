class Solution:
    # @param A : list of strings
    # @return a strings
    def serialize(self, A):
        s=''
        for i in A:
            s=s+i+str(len(i))+'~'
        return s
