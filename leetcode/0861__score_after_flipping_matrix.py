from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        """
        Discussion:
        - We would most likely want that first bit in each of the numbers
          to be 1. So we can start by flipping each row if its first bit
          is 0.
        - Next, we probably want more 1's than 0's in each subsequent column

        >>> s = Solution()
        >>> s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
        39
        >>> s.matrixScore([[0]])
        1
        """

        # print(grid)

        numRows = len(grid)
        numCols = len(grid[0])

        for row in range(numRows):
            if grid[row][0] == 0:
                self.flipRow(grid, row)

        # print(grid)

        for col in range(numCols):
            numOnes = 0
            for row in range(numRows):
                numOnes += grid[row][col]
            if numOnes <= numRows // 2:
                self.flipCol(grid, col)

        # print(grid)

        total = 0
        for row in grid:
            total += self.toNumber(row)
        return total

    def toNumber(self, bits: list[int]) -> int:
        return int(''.join([str(i) for i in bits]), 2)

    def flipRow(self, grid: list[list[int]], row: int) -> None:
        for col in range(len(grid[row])):
            # grid[row][col] = 0 if grid[row][col] == 1 else 1
            grid[row][col] ^= 1
    
    def flipCol(self, grid: list[list[int]], col: int) -> None:
        for row in range(len(grid)):
            grid[row][col] = 0 if grid[row][col] == 1 else 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
