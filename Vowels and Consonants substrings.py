# This solution gives us memory limit exceeeded error

class Solution:
    # @param A : string
    # @return an integer
    def isvowel(self,s):
        if 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s:
            return True
        return False
        
    def solve(self, A):
        lst=[]
        for i in range(len(A)):
            for j in range(i+1,len(A)+1):
                substring=A[i:j]
                if (self.isvowel(substring[0]) and not self.isvowel(substring[-1])) or (not self.isvowel(substring[0]) and self.isvowel(substring[-1])):
                    lst.append(substring)
        return len(lst) % (10**7)

