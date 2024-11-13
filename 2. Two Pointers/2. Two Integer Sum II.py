class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, f = 0, len(numbers) - 1

        while i < f:
            curr = numbers[i] + numbers[f]

            if curr < target:
                i += 1
            elif curr > target:
                f -= 1
            else: 
                return [i + 1, f + 1]
        return []