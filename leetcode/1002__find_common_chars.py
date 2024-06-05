from typing import List

"""
Given a string array words, return an array of all characters that show up in
all strings within the words (including duplicates). You may return the answer
in any order.

Example 1:

Input: words = ["bella","label","roller"]

Output: ["e","l","l"]

Example 2:

Input: words = ["cool","lock","cook"]

Output: ["c","o"]

Constraints:

- 1 <= words.length <= 100

- 1 <= words[i].length <= 100

- words[i] consists of lowercase English letters.

"""
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        >>> s = Solution()
        >>> sorted(s.commonChars(["bella", "label", "roller"]))
        ['e', 'l', 'l']
        >>> sorted(s.commonChars(["cool", "lock", "cook"]))
        ['c', 'o']
        """
        return self.commonChars1(words)

    def commonChars1(self, words: list[str]) -> list[str]:
        """
        To find all common characters across all words (not including
        duplicates), simply find the intersection of all characters across
        all words.

        To find all the common characters across all words including duplicates,
        need to keep track of the minimum number of occurrences of a character
        across all words.

        Time:
        - m = len(words)
        - n = length (max? avg? of any given word in words
        - O(m) * O(n) to iterate through all characters in all words to
          count occurrences and identify common
        - O(m) * O(n) to calculate set differences
        - O(n) to assemble result (look up char frequency for common chars)
        - => O(m * n)

        Space:
        - Common chars all words = O(m * n)
        - Min common char freq = O(m * n)
        - => O(m * n)
        """

        commonCharsAllWords = None
        minCommonCharFreq = {}
        for word in words:
            charsInWord = {}
            for c in word:
                if c in charsInWord:
                    charsInWord[c] += 1
                else:
                    charsInWord[c] = 1

            if commonCharsAllWords is None:
                commonCharsAllWords = set(charsInWord.keys())
            else:
                commonCharsAllWords &= set(charsInWord.keys())

            for c, cnt in charsInWord.items():
                if c in minCommonCharFreq:
                    minCommonCharFreq[c] = min(cnt, minCommonCharFreq[c])
                else:
                    minCommonCharFreq[c] = cnt

        # print(f"commonCharsAllWords={commonCharsAllWords}")
        # print(f"minCommonCharFreq={minCommonCharFreq}")

        result = []
        for c in commonCharsAllWords:
            for i in range(minCommonCharFreq[c]):
                result.append(c)
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
