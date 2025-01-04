from typing import List

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        >>> s = Solution()
        >>> s.countPalindromicSubsequence("aabca")
        3
        >>> s.countPalindromicSubsequence("adc")
        0
        >>> s.countPalindromicSubsequence("bbcbaba")
        4
        """
        return self.countPalindromicSubsequence1(s)

    def countPalindromicSubsequence1(self, s: str) -> int:
        """
        - Start from left i = 0
        - If we've seen s[i], go to next char
        - Otherwise
          - Start from right j = len(s) - 1
          - Decrementing j, try to find s[j] == s[i]
          - If found, count unique chars in s from i+1 to j-1, and add that
            to count
          - If j gets down to i + 1 without match, can't make 3-char palindrome
            any more, so go to next ith char
        """
        numPalindromicSubsequences = 0
        i = 0
        firstCharSeen = set()
        while i < len(s) - 2:
            if s[i] not in firstCharSeen:
                firstCharSeen.add(s[i])
                j = len(s) - 1
                while j >= i + 2:
                    if s[j] == s[i]:
                        uniqueChars = set(s[i + 1:j])
                        numPalindromicSubsequences += len(uniqueChars)
                        break
                    j -= 1
            i += 1
        return numPalindromicSubsequences

if __name__ == '__main__':
    import doctest
    doctest.testmod()
