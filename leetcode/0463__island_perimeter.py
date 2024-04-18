from typing import List, Generator

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Number of neighbors determine number of edges contributing to perimeter?
        - 1 neighbor  = 3
        - 2 neighbors = 2
        - 3 neighbors = 1
        - 4 neighbors = 0

        - maintain neighbors 2x2 array
        - for each cell in grid, increment neighbors count for all cells around it
        - then, for each land cell in grid, count neighbors to determine edges
          that contribute to perimeter
        
        Time:
        - m = rows
        - n = cols
        - m*n = cells
        - O(m*n) to iterate through each cell in grid, O(1) to increment neighbor counts
        - O(m*n) to iterate through each cell in grid to locate land and accumulate
          perimeter
        - => O(m*n)

        Space:
        - m = rows
        - n = cols
        - O(m*n) neighbors storage

        >>> s = Solution()
        >>> s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
        16
        """
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [ [0 for x in range(cols)] for y in range(rows) ]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    for (n_row, n_col) in self.generateNeighborCoords(row, col, rows, cols):
                        neighbors[n_row][n_col] += 1
        # print(f"{neighbors}")

        perimeter = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    perimeter += (4 - neighbors[row][col])
        return perimeter
    
    def generateNeighborCoords(self, row: int, col: int, rows: int, cols: int) -> Generator[tuple[int, int], None, None]:
        if row > 0:
            yield [row - 1, col]
        if row < rows - 1:
            yield [row + 1, col]
        if col > 0:
            yield [row, col - 1]
        if col < cols - 1:
            yield [row, col + 1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
