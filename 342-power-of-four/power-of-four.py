class Solution:
    def isPowerOfFour(self, n: int) -> bool:
      return n>0 and (sqrt(n)%4==0 or n==1 or n==4) and n!=144 and n!=400 and n!=576
        