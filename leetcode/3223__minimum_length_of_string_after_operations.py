class Solution:
    def minimumLength(self, s: str) -> int:
        """
        >>> s = Solution()
        >>> s.minimumLength('abaacbcbb')
        5
        >>> s.minimumLength('aa')
        2
        """
        return self.minimumLength1(s)

    def minimumLength1(self, s: str) -> int:
        """
        Basically, the operation removes a pair of the same letter if there
        is that letter in between.

        - Count frequencies of letters
        - If letter occurs odd number of times, can reduce to 1 (given 2n + 1
          of the same letter in s, we can find an i such that n of that letter
          is to the left of index i and n is to the right)
        - If letter occurs even number of times, can reduce to 2 (given 2n
          of the same letter, we can find an i such that n - 1 of that letter
          is to the left of index i and in is to the right, but we would
          get to the point where we have a minimum 2 of that letter and can
          therefore no longer apply the operation)

        Time:
        - n = len(s)
        - O(n) to iterate through s and count letter frequencies
        - O(1) to determine minimum frequency for a given letter based
          on the above
        - => O(n)

        Space:
        - n = len(s)
        - O(1) list of letter frequencies (always 26 elements)
        - O(1) for constants
        - => O(1)
        """
        letterFrequencies = [0 for c in 'abcdefghijklmnopqrstuvwxyz']
        ordA = ord('a')
        for c in s:
            letterFrequencies[ord(c) - ordA] += 1

        minLen = 0
        for freq in letterFrequencies:
            if freq > 0:
                if freq % 2 == 1:
                    minLen += 1
                else:
                    minLen += 2
        return minLen

if __name__ == '__main__':
    import doctest
    doctest.testmod()
