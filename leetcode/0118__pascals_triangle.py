from typing import List, Generator

"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above
it.

[1]
[1,1]
[1,2,1]
[1,3,3,1]
...
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return list(self.generateGenerator(numRows))

    # Generator method that emits row by row
    def generateGenerator(self, numRows: int) -> Generator[List[int], None, None]:
        """
        Strategy: Create a generator that emits each row of Pascal's Triangle
        from 1..n. The generator simply needs to keep track of the previous
        row in order to generate the next row.
        """
        prev = None
        for i in range(1, numRows + 1):
            row = [1 for x in range(i)]
            for j in range(1, i - 1):
                row[j] = prev[j - 1] + prev[j]
            yield row
            prev = row

if __name__ == '__main__':
    s = Solution()
    print(*(s.generate(10)), sep="\n")

