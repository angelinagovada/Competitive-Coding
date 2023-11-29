class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            j = bin(i)
            x = str(j)
            y = x.count('1')

            print(i)
            print(j)
            print(x)
            print(y)

            ans.append(y)

        
        return ans 
        