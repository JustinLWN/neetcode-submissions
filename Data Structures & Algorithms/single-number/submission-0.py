class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for i in nums:
            if i not  in result:
                result[i] = 0
            result[i] += 1
        for key, value in result.items():
            if value == 1:
                return key