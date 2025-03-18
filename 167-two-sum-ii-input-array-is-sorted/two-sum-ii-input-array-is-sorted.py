class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        left = 0
        right = N-1

        while(right>left):
            if( numbers[left] + numbers[right] == target ):
                return [left+1, right+1]
            elif(numbers[left] + numbers[right]> target):
                right-=1
            else:
                left+=1


        return [left+1, right+1]

        