from collections import defaultdict
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        >>> s = Solution()
        >>> s.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"])
        ['facebook', 'google', 'leetcode']
        >>> s.wordSubsets(["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"])
        ['apple', 'google', 'leetcode']
        """
        return self.wordSubsets2(words1, words2)

    def wordSubsets1(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        - dict from character and multiplicity to list of matching words in words1
        - for each word in words2, split words into char and multiplicity parts,
          see which words have the same char and multiplicity, and keep calculating
          the intersection of these sets
        - convert final set to a list
        """
        partsToWords1 = defaultdict(set)
        for word in words1:
            parts = self.splitWord(word)
            for part in parts:
                partAccum = ''
                for c in part:
                    partAccum += c
                    partsToWords1[partAccum].add(word)
        # print(partsToWords1)

        universalStrings = set(words1)
        for word in words2:
            parts = self.splitWord(word)
            for part in parts:
                universalStrings &= partsToWords1[part]
            # print(f"SO FAR {universalStrings}")
        return sorted(list(universalStrings))

    def splitWord(self, word: str) -> list[str]:
        parts = []
        chars = sorted(word)
        part = None
        for c in chars:
            if part is None:
                part = c
            elif part[0] == c:
                part += c
            else:
                parts.append(part)
                part = c
        parts.append(part)
        return parts

    def wordSubsets2(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        Suggested optimization here is to calculate the max occurences of each character for each
        word in words2. Then for each word in words1, calculate its character frequency, and
        make sure that each character appears that many times in the words2 character frequency map.
        """

        maxCharFrequenciesWords2 = dict()

        for word in words2:
            parts = self.splitWord(word)
            for part in parts:
                if part[0] not in maxCharFrequenciesWords2:
                    maxCharFrequenciesWords2[part[0]] = len(part)
                else:
                    maxCharFrequenciesWords2[part[0]] = max(maxCharFrequenciesWords2[part[0]], len(part))
        # print(maxCharFrequenciesWords2)
        universalWords = []
        for word in words1:
            charFreq = dict()
            parts = self.splitWord(word)
            for part in parts:
                charFreq[part[0]] = len(part)

            isUniversal = True
            for c, freq in maxCharFrequenciesWords2.items():
                if c not in charFreq or charFreq[c] < maxCharFrequenciesWords2[c]:
                    # print(f"{c} not in {word}")
                    isUniversal = False
                    break
            if isUniversal:
                universalWords.append(word)
        return universalWords

if __name__ == '__main__':
    import doctest
    doctest.testmod()
