from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        >>> s = Solution()
        >>> s.countPrefixSuffixPairs(["a","aba","ababa","aa"])
        4
        >>> s.countPrefixSuffixPairs(["pa","papa","ma","mama"])
        2
        >>> s.countPrefixSuffixPairs(["abab","ab"])
        0
        >>> s.countPrefixSuffixPairs(["a", "abb"])
        0
        """
        return self.countPrefixSuffixPairs2(words)

    def countPrefixSuffixPairs1(self, words: List[str]) -> int:
        """
        Execute the algorithm as laid out -- with 0 <= i < j < len(words), count
        all (i, j) pairs such that words[i] is both a prefix and a suffix of words[j]
        """
        count = 0
        i = 0
        while i < len(words):
            j = i + 1
            while j < len(words):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    count += 1
                j += 1
            i += 1
        return count

    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        # print(f"isPrefixAndSuffix(str1={str1}, str2={str2})")
        if len(str1) > len(str2):
            # print(f"FALSE")
            return False
        isMatch = self.matches(str1, str2, 0) and \
            self.matches(str1, str2, len(str2) - len(str1))
        # print(f"isMatch={isMatch}")
        return isMatch

    def matches(self, str1: str, str2: str, startIndex: int) -> bool:
        """
        Compare str1 and str2 to see if str1 is a substring of str2 starting at
        startIndex. Requires that len(str1) <= len(str2).
        """
        for i in range(len(str1)):
            if str1[i] != str2[startIndex + i]:
                return False
        return True

    def countPrefixSuffixPairs2(self, words: List[int]) -> int:
        """
        Use built-in startswith() and endswith() rather than rolling own
        """
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) <= len(words[j]) and \
                   words[j].startswith(words[i]) and \
                   words[j].endswith(words[i]):
                    count += 1
        return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
