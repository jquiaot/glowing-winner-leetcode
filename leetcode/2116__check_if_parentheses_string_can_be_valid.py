class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        >>> s = Solution()
        >>> s.canBeValid("))()))", "010100")
        True
        >>> s.canBeValid("()()", "0000")
        True
        >>> s.canBeValid(")", "0")
        False
        """
        return self.canBeValid1(s, locked)

    def canBeValid1(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        op = 0
        cp = 0
        for i in range(len(s)):
            if locked[i] == '0' or s[i] == '(':
                op += 1
            else:
                op -= 1
            if op < 0:
                return False
        for i in range(len(s) - 1, -1 , -1):
            if locked[i] == '0' or s[i] == ')':
                cp += 1
            else:
                cp -= 1
            if cp < 0:
                return False
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
