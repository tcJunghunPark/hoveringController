class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remain = 0
        for i in range(len(nums)):
            if not self.isLarger(nums[i], target):
                remain = target - nums[i]
                for j in range(i+1, len(nums)):
                    if remain == nums[j]:
                        return [i, j]
    
    
    def isLarger(self, num, target):
        return num > target

sol = Solution()
print(sol.twoSum([-1,-2,-3,-4,-5], -8))