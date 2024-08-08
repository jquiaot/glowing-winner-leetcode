from typing import List, Generator

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        """
        >>> s = Solution()
        >>> s.spiralMatrixIII(1, 4, 0, 0)
        [[0, 0], [0, 1], [0, 2], [0, 3]]
        >>> s.spiralMatrixIII(5, 6, 1, 4)
        [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]
        """
        hit_max_x = False
        hit_max_y = False
        hit_min_x = False
        hit_min_y = False
        min_x = 0
        max_x = cols - 1
        min_y = 0
        max_y = rows - 1

        output = []
        for c in self.generateSpiral():
            c[0] += rStart
            c[1] += cStart
            if hit_max_x and hit_max_y and hit_min_x and hit_min_y:
                break
            if c[1] < min_x:
                hit_min_x = True
            elif c[1] > max_x:
                hit_max_x = True
            elif c[0] < min_y:
                hit_min_y = True
            elif c[0] > max_y:
                hit_max_y = True
            else:
                output.append(c)
        return output

    """
    Generate (x, y) coordinates following an expanding spiral centered at (0, 0)

    0,0
    0,1
    1,1
    1,0
    1,-1
    0,-1
    -1,-1
    -1,0
    -1,1
    -1,2
    0,2
    1,2
    2,2
    ...
    """
    def generateSpiral(self) -> Generator[list[int, int], None, None]:
        cur_x = 0
        cur_y = 0
        min_x = -1
        min_y = -1
        max_x = 1
        max_y = 1

        while True:
            while cur_x < max_x:
                yield [cur_y, cur_x]
                cur_x += 1
            while cur_y < max_y:
                yield [cur_y, cur_x]
                cur_y += 1
            while cur_x > min_x:
                yield [cur_y, cur_x]
                cur_x -= 1
            while cur_y > min_y:
                yield [cur_y, cur_x]
                cur_y -= 1

            min_x -= 1
            min_y -= 1
            max_x += 1
            max_y += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()


