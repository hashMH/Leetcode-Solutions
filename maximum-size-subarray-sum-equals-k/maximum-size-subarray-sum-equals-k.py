class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pre_sums = {}
        max_size = 0
        rs = 0
        for i in range(len(nums)):
            rs += nums[i]
​
            if rs == k:
                max_size = max(max_size, i+1)
            elif rs-k in pre_sums:
                max_size = max(max_size, i - pre_sums[rs-k])
            
            if rs not in pre_sums:
                pre_sums[rs] = i
        return max_size
