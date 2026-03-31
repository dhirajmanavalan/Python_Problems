'''Product of Array Except Self'''
def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result


print(product_except_self([1,2,3,4]))
# Output: [24,12,8,6]