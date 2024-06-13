from typing import List

"""
There are n seats and n students in a room. You are given an array seats of
length n, where seats[i] is the position of the ith seat. You are also given
the array students of length n, where students[j] is the position of the jth
student.

You may perform the following move any number of times:

- Increase or decrease the position of the ith student by 1 (i.e., moving the
  ith student from position x to x + 1 or x - 1)

Return the minimum number of moves required to move each student to a seat such
that no two students are in the same seat.

Note that there may be multiple seats or students in the same position at the
beginning.

Example 1:

Input: seats = [3,1,5], students = [2,7,4]

Output: 4

Explanation: The students are moved as follows:

- The first student is moved from from position 2 to position 1 using 1 move.

- The second student is moved from from position 7 to position 5 using 2 moves.

- The third student is moved from from position 4 to position 3 using 1 move.
In total, 1 + 2 + 1 = 4 moves were used.

Example 2:

Input: seats = [4,1,5,9], students = [1,3,2,6]

Output: 7

Explanation: The students are moved as follows:

- The first student is not moved.

- The second student is moved from from position 3 to position 4 using 1 move.

- The third student is moved from from position 2 to position 5 using 3 moves.

- The fourth student is moved from from position 6 to position 9 using 3 moves.

In total, 0 + 1 + 3 + 3 = 7 moves were used.

Example 3:

Input: seats = [2,2,6,6], students = [1,3,2,6]

Output: 4

Explanation: Note that there are two seats at position 2 and two seats at
position 6.

The students are moved as follows:

- The first student is moved from from position 1 to position 2 using 1 move.

- The second student is moved from from position 3 to position 6 using 3 moves.

- The third student is not moved.

- The fourth student is not moved.

In total, 1 + 3 + 0 + 0 = 4 moves were used.

Constraints:

- n == seats.length == students.length

- 1 <= n <= 100

- 1 <= seats[i], students[j] <= 100
"""
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.minMovesToSeat([3, 1, 5], [2, 7, 4])
        4
        >>> s.minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6])
        7
        >>> s.minMovesToSeat([2, 2, 6, 6], [1, 3, 2, 6])
        4
        """
        return self.minMovesToSeat1(seats, students)

    def minMovesToSeat1(self, seats: list[int], students: list[int]) -> int:
        """
        Discussion: We can sort both the seats and the students. This will
        line up the seats and students to their most likely closest seat.
        Then we just need to calculate the number of moves between the ith
        student and ith seat (absolute value of difference).

        Time:
        - n = len(students) (or len(seats), should be the same)
        - O(n*lg(n)) to sort seats
        - O(n*lg(n)) to sort studetns
        - O(n) to iterate through students and calculate difference
        - => O(n*lg(n))

        Space:
        - n = len(students)
        - O(1) no aux space except for output moves
        """
        moves = 0

        seats.sort()
        students.sort()

        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])
        return moves

if __name__ == '__main__':
    import doctest
    doctest.testmod()
