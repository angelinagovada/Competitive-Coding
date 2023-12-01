class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ""

        for i in digits:
            n = n+str(i)

        n1 = int(n)+1

        n2 = [int(j) for j in str(n1)]

        return n2


        