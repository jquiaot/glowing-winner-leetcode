"""
You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of
s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting
some or no characters without changing the order of the remaining characters.

Example 1:

Input: s = "coaching", t = "coding"

Output: 4

Explanation: Append the characters "ding" to the end of s so that s =
"coachingding".

Now, t is a subsequence of s ("coachingding").

It can be shown that appending any 3 characters to the end of s will never make
t a subsequence.

Example 2:

Input: s = "abcde", t = "a"

Output: 0

Explanation: t is already a subsequence of s ("abcde").

Example 3:

Input: s = "z", t = "abcde"

Output: 5

Explanation: Append the characters "abcde" to the end of s so that s =
"zabcde".  Now, t is a subsequence of s ("zabcde").

It can be shown that appending any 4 characters to the end of s will never make
t a subsequence.

Constraints:

- 1 <= s.length, t.length <= 105

- s and t consist only of lowercase English letters.
"""
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        >>> s = Solution()
        >>> s.appendCharacters("coaching", "coding")
        4
        >>> s.appendCharacters("lbg", "g")
        0
        """
        return self.appendCharacters1(s, t)

    def appendCharacters1(self, s: str, t: str) -> int:
        """
        Iterate through s, finding letters of t that match. If we exhaust
        all letters of t, then we've found all the characters of t in
        s in the order found in t, and so ti will equal len(t), and as
        expected we should return 0 (t is a subsequence of s). If, however,
        we didn't find all letters of t in s, then the difference between
        the length of t and the number of letters we found should be the
        number of chars we need to append to s to get t to be a subsequence.

        Time:
        - m = len(s), n = len(t)
        - O(m + n) to iterate through s and t to find subsequence and
          missing chars
        - => O(m + n)

        Space:
        - => O(1) aux space for s and t pointers
        """
        si = 0
        ti = 0
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                ti += 1
            si += 1
        return len(t) - ti

if __name__ == '__main__':
    import doctest
    doctest.testmod()
