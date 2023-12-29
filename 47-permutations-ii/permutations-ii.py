class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        p = permutations(nums)
        ans = []

        for i in p:
            #print(list(i))
            x = list(i)
            if x not in ans:
                ans.append(list(i))

        return list(ans)   