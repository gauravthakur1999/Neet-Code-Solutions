class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in nums:
            curr_len = 0
            if num - 1 not in num_set:
                curr_len += 1
                new = num
                while new + 1 in num_set:
                    curr_len +=1
                    new += 1
            max_len = max(curr_len, max_len)
        
        return max_len
        