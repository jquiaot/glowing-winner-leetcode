from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        >>> s = Solution()
        >>> s.vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]])
        [2, 3, 0]
        >>> s.vowelStrings(["a","e","i"], [[0,2],[0,1],[2,2]])
        [3, 2, 1]
        """
        return self.vowelStrings1(words, queries)

    def vowelStrings1(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        1. Create a list validWords, where the ith value in validWords is 1 if the 1th value in words starts 
           and ends with a vowel, 0 otherwise
           ["aba", "bcb"] => [1, 0]
        2. For each query, sum up the values in validWords from the query start and end value
        """
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        validWords = []
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                validWords.append(1)
            else:
                validWords.append(0)
        answers = []
        for query in queries:
            answers.append(sum(validWords[query[0]:query[1] + 1]))
        return answers

if __name__ == '__main__':
    import doctest
    doctest.testmod()
