'Median of Two Sorted Arrays (Binary Search)'
nums1 = [1,3]
nums2 = [2]

nums = sorted(nums1 + nums2)
n = len(nums)

if n % 2 == 0:
    median = (nums[n//2 - 1] + nums[n//2]) / 2
else:
    median = nums[n//2]

print("Median:", median)