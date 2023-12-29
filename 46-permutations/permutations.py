class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        p = permutations(nums)
        ans = []

        for i in p:
            print(list(i))
            ans.append(list(i))


        return list(ans)

        