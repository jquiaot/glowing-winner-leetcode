from typing import List

class Solution:
    """
    Iterate through the list of words and check if each is a palindrome. If
    a palindrome is found, return it.

    Time:
    - O(n) to iterate through list of n words
    - O(m) for each word to compare letters, where m is max word length
    - => O(n * m)

    Space:
    - O(1) no auxilliary space needed

    >>> s = Solution()
    >>> s.firstPalindrome(["abc","car","ada","racecar","cool"])
    'ada'
    >>> s.firstPalindrome(["notapalindrome","racecar"])
    'racecar'
    >>> s.firstPalindrome(["def", "ghi"])
    ''
    """
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if self.isPalindrome(w):
                return w
        return ""

    """
    Returns true iff the specified word is a palindrome. Determine this by
    comparing letters from the start and end of the word, moving towards
    the center.
    """
    def isPalindrome(self, word: str) -> bool:
        start = 0
        end = len(word) - 1
        while start <= end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()

