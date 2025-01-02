class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set() # the final max possible triplet for target triplet

        for t in triplets: # iterate through all triplets 
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]: # if tiplet has value more than target triplet don't use it
                continue 
            for i, v in enumerate(t):
                if v == target[i]: # if tiplet has value equal to target triplet add it to good
                    good.add(i)
        return len(good) == 3
    
# Greedy implementation Optimal

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False
        for t in triplets:
            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])
            y |= (t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2])
            z |= (t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2])
            if x and y and z:
                return True
        return False