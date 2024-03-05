"""
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked
to apply the following algorithm on the string any number of times:

1. Pick a non-empty prefix from the string s where all the characters in the
prefix are equal.

2. Pick a non-empty suffix from the string s where all the characters in this
suffix are equal.

3. The prefix and the suffix should not intersect at any index.

4. The characters from the prefix and suffix must be the same.

5. Delete both the prefix and the suffix.

Return the minimum length of s after performing the above operation any number
of times (possibly zero times).
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        """
        Maintain two pointers, at start and end of s.
        While the two pointers do not cross, check characters pointed at:
        - If not the same, break (can't perform any moves)
        - If the same, then attempt to strip off characters until characters
          change or pointers cross

        Time:
        - Let n = len(s)
        - => O(n) traverse chars in s at most once

        Space:
        - Let n = len(s)
        - => O(1) for the two pointers

        >>> s = Solution()
        >>> s.minimumLength("ca")
        2
        >>> s.minimumLength("cabaabac")
        0
        >>> s.minimumLength("aabccabba")
        3
        >>> s.minimumLength("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        0
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                break
            c = s[i]
            while i < j and s[i] == c:
                i += 1
            while j >= i and s[j] == c:
                j -= 1
        return max(0, j - i + 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
