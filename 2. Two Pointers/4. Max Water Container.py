class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_size = 0
        l, r = 0, len(heights) -1

        while l < r:
            curr_size = min(heights[l], heights[r]) * (r - l)

            if curr_size >= max_size:
                max_size = curr_size
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_size 