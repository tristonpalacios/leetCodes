import math

def productExceptSelf( nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    # Calculate suffix products and multiply with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

def productExceptSelf(self, nums: list[int]) -> list[int]:
    vals = [0] * len(nums)
    zero_count = nums.count(0)

    if zero_count > 1:
        return vals

    if zero_count == 1:
        idx = nums.index(0)
        # Calculate the product of all non-zero elements
        prod = 1
        for num in nums:
            if num != 0:
                prod *= num
        vals[idx] = prod
        return vals

    # No zeros in the list, calculate the product of all elements
    prod = math.prod(nums)
    for i, val in enumerate(nums):
        vals[i] = prod // nums[i]

    return vals

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))