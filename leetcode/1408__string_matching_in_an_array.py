from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        >>> s = Solution()
        >>> s.stringMatching(["mass","as","hero","superhero"])
        ['as', 'hero']
        >>> s.stringMatching(["leetcode","et","code"])
        ['et', 'code']
        >>> s.stringMatching(["blue","green","bu"])
        []
        """
        return self.stringMatching1(words)

    def stringMatching1(self, words: List[str]) -> List[str]:
        """
        Simple string comparisons. We'll sort the list of words
        by length (increasing).

        Time:
        - n = len(words)
        - O(n*lg(n)) to sort
        - O(n) iterate through words
        - O(n) to find if substring in other words
        - => O(n^2)
        """
        words.sort(key = len)

        substringWords = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    substringWords.append(words[i])
                    break

        return substringWords

if __name__ == '__main__':
    import doctest
    doctest.testmod()
