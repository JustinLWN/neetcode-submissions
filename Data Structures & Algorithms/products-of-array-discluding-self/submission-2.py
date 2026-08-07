class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count, product = 0, 1 
        for num in nums:
            if num != 0:
                product *= num
            else: 
                count += 1 
        
        result = []

        match count:
            case 0:
                for num in nums:
                    result.append(int (product/num))        
            case 1:
                for num in nums:
                    if num == 0:
                        result.append(product)
                    else:
                        result.append(0)
            case _:
                result = [0] * len(nums)

        return result
         