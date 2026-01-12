from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        >>> s = Solution()
        >>> s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
        7
        >>> s.minTimeToVisitAllPoints([[3,2],[-2,2]])
        5
        """
        return self.min_time_to_visit_all_points_1(points)

    def min_time_to_visit_all_points_1(self, points: list[list[int]]) -> int:
        """
        For each pair of points in order, calculate the min steps.

        Time:
        - n = len(points)
        - O(n) step through n and check consecutive pairs of points
        - O(1) for calculating min steps per pair
        - => O(n)

        Space:
        - n = len(points)
        - O(1) storage for pairwise steps calculation
        - O(1) storage for total time (return value)
        - => O(1)
        """
        if points is None or len(points) == 0:
            return 0
        total_time = 0
        for i in range(len(points) - 1):
            total_time += self.min_time_between_points(points[i], points[i + 1])
        return total_time

    def min_time_between_points(self, a: list[int], b: list[int]) -> int:
        """
        1. Take as many diagonals as we can (until a[0] == b[0] or a[1] == b[1])
           - Should be able to just take the diffs of x values and y values, and so number
             of diagonals we can take is the smallest diff
        2. Remaining steps should be horizontal or vertical steps
           - Should be able to take max x/y diff and substract number of diagonals
        3. Sum the diagonals and straight steps
        """
        x_diff = abs(a[0] - b[0])
        y_diff = abs(a[1] - b[1])
        diagonals = min(x_diff, y_diff)
        straight_part = abs(max(x_diff, y_diff) - diagonals)
        return straight_part + diagonals

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# END
