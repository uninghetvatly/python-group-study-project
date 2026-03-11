# Rotate array
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        
nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
print(nums)