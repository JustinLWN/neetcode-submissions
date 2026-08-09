class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, result = [], [], []
        l = len(nums)
        for i in range(l):
            if i == 0:
                left.append(1)
            else:
                left.append(left[i - 1] * nums[i - 1])
                
        for i in range(l - 1, -1 , -1):
            if i == l - 1:
                right.append(1)
            else:
                right.append(right[-1] * nums[i +1])
        right.reverse()

        for i in range(l):
            result.append(left[i]*right[i])

        return result