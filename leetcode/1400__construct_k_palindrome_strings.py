from collections import defaultdict

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        >>> s = Solution()
        >>> s.canConstruct("annabelle", 2)
        True
        >>> s.canConstruct("leetcode", 3)
        False
        >>> s.canConstruct("true", 4)
        True
        """
        return self.canConstruct2(s, k)

    def canConstruct1(self, s: str, k: int) -> bool:
        """
        Discussion:
        - Max number of palindromes that can be made should be len(s)
          (each char in its own palindrome string)
        - Min number of palindromes that can be made should be the
          number of odd character counts (each odd-count character can
          be combined with any number of even-count characters in pairs
          in order to make a palindrome, but odd-count characters can't
          be combined with other odd-count characters)
        """
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1

        charsWithOddCounts = 0
        charsWithEvenCounts = 0
        for c, cnt in counts.items():
            if cnt % 2 == 0:
                charsWithEvenCounts += 1
            else:
                charsWithOddCounts += 1

        # print(f"odd={charsWithOddCounts}")
        return charsWithOddCounts <= k and k <= len(s)

    def canConstruct2(self, s: str, k: int) -> bool:
        """
        Try to optimize counting by using a list and indexes
        rather than a dict.
        """
        counts = [0 for c in 'abcdefghijklmnopqrstuvwxyz']
        ord_a = ord('a')
        for c in s:
            counts[ord(c) - ord_a] += 1

        oddCounts = 0
        for i in range(len(counts)):
            if counts[i] % 2 == 1:
                oddCounts += 1

        return oddCounts <= k and k <= len(s)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
