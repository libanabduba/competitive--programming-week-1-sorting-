class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            for j in range(len(i) - 1,-1,-1):
                if i[j] < 0:
                    count += 1
        return count
