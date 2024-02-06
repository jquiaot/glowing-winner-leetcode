"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Strategy:
        - Maintain a dict from str(sorted(s)) to list[str]
        - For each word in strs
            - Sort letters as a string
            - Find list with sorted letters string and add orig word to list
        - Collect values of dict for return

        Time:
        - let n = len(strs)
        - let m = max(len(strs[i]))
        - O(n) to iterate through strs
        - O(m*lg(m) * n) to sort the words
        - => Should go to O(n) for sufficiently large n, O(m*lg(m)) becomes some small constant
        - O(1) to insert into dict()
        - O(n) to collect values
        - => O(n) final time complexity

        Space:
        - O(n) dict storage

        >>> s = Solution()
        >>> sorted([sorted(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))])
        [[['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']]]
        """
        anagramGroups = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in anagramGroups:
                anagramGroups[sortedWord] = []
            anagramGroups[sortedWord].append(word)

        if len(anagramGroups) == 0:
            return []
        else:
            return list(anagramGroups.values())

if __name__ == '__main__':
    import doctest
    doctest.testmod()

