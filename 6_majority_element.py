class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        sorted_nums = set(nums)
        n = len(nums)
        
        for x in sorted_nums:
            if nums.count(x) > n/2:
                return x