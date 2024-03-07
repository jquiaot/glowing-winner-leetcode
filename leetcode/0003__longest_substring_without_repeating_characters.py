"""
Given a string s, find the length of the longest substring without repeating
characters.

Example 1:

Input: s = "abcabcbb"

Output: 3

Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"

Output: 1

Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"

Output: 3

Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a
substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        >>> s = Solution()
        >>> s.lengthOfLongestSubstring("abcabcbb")
        3
        >>> s.lengthOfLongestSubstring("bbbbb")
        1
        >>> s.lengthOfLongestSubstring("pwwkew")
        3
        >>> s.lengthOfLongestSubstring("dvdf")
        3
        """
        return self.lengthOfLongestSubstring2(s)

    def lengthOfLongestSubstring1(self, s: str) -> int:
        """
        Naive solution: Calculate longest unique substring for each point
        from 0 to len(s).

        Time:
        - n = len(s)
        - m = num chars to traverse to determine uniqueness (potentially n
              if the character domain is sufficiently large)
        - => O(n*m)
        Space:
        - n = len(s)
        - => O(n) if all chars are unique, then potentially storing n chars
        """
        maxLen = 0
        for i in range(len(s)):
            seenChars = set()
            for j in range(i, len(s)):
                if s[j] in seenChars:
                    if maxLen < len(seenChars):
                        maxLen = len(seenChars)
                    break
                else:
                    seenChars.add(s[j])
        return maxLen

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        Sliding window solution: Maintain a sliding window for identifying
        the longest unique substring.

        Use two pointers -- one pointing to the head of the window and one
        pointing to the tail of the window. Initially head and tail pointing
        to char 0.

        Maintain a set of unique characters.

        Add chars from head to set, advancing head as long as the new char
        isn't present in set.

        When head char is present in set, note max length, and remove
        chars at tail from set, advancing tail until we encounter the
        head char. Advance tail one more, and then continue again with head.

        Time:
        - n = len(s)
        - => O(n) traverse s once to see all chars and identify longest unique
        Space:
        - n = len(s)
        - => O(n) worse case if all chars are unique
        """
        if len(s) == 0:
            return 0
        maxLen = 0
        head = 0
        tail = 0
        uniqueChars = set()
        while head < len(s):
            if s[head] not in uniqueChars:
                # keep adding chars from head until we find non-unique
                uniqueChars.add(s[head])
                head += 1
            else:
                # check if this is new maxLen
                if maxLen < len(uniqueChars):
                    maxLen = len(uniqueChars)
                while tail < head:
                    # keep advancing tail towards head, removing chars
                    # from uniqueChars until we encounter the same char
                    # as head
                    if s[tail] == s[head]:
                        uniqueChars.remove(s[tail])
                        tail += 1
                        break
                    else:
                        uniqueChars.remove(s[tail])
                        tail += 1

        if maxLen < len(uniqueChars):
            maxLen = len(uniqueChars)
        return maxLen

if __name__ == '__main__':
    import doctest
    doctest.testmod()
