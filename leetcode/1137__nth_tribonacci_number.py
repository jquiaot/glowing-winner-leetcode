class Solution:
    def tribonacci(self, n: int) -> int:
        """
        >>> s = Solution()
        >>> s.tribonacci(4)
        4
        >>> s.tribonacci(25)
        1389537
        """
        return self.tribonacci2(n)
    
    def tribonacci1(self, n: int) -> int:
        """
        Attempt 1: Use a list to tabulate tribonacci values
        from 0..n.

        Time: O(n)
        Space: O(n)
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            values = [0 for i in range(n + 1)]
            values[1] = 1
            values[2] = 1
            for i in range(3, n + 1):
                values[i] = values[i - 3] + values[i - 2] + values[i - 1]
            return values[n]

    def tribonacci2(self, n: int) -> int:
        """
        Attempt 2: Just keep track of the last 3 values computed, shifting
        down accordingly.

        Time: O(n)
        Space: O(1) (always holding just the previous 3 values)
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            a = 0
            b = 1
            c = 1
            v = 2
            for i in range(3, n + 1):
                v = a + b + c
                a = b
                b = c
                c = v
            return v

if __name__ == '__main__':
    import doctest
    doctest.testmod()
