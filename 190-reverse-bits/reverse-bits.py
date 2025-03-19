class Solution:
    def reverseBits(self, n: int) -> int:
        n1 = f"{n:032b}"
        n2 = n1[::-1]
        print(n2)
        return int(n2,2)

        