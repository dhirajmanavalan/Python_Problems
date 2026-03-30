'''Maximum Product Subarray'''

def max_product(nums):
    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        temp = max(num, max_prod * num, min_prod * num)
        min_prod = min(num, max_prod * num, min_prod * num)
        max_prod = temp
        result = max(result, max_prod)

    return result

print(max_product([2,3,-2,4]))  # 6