class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        x="{:032b}".format(A)
        y=x[::-1]
        return int(y,2)
  # Note : int() consists of the second parameter as well 
  # int(value to be converted to int, base of the value that has to be converted to int)
