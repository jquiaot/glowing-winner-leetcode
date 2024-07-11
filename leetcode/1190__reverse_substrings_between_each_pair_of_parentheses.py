from collections import deque
from typing import List

"""
You are given a string s that consists of lower case English letters and
brackets.

Reverse the strings in each pair of matching parentheses, starting from the
innermost one.

Your result should not contain any brackets.

Example 1:

Input: s = "(abcd)"

Output: "dcba"

Example 2:

Input: s = "(u(love)i)"

Output: "iloveu"

Explanation: The substring "love" is reversed first, then the whole string is
reversed.

Example 3:

Input: s = "(ed(et(oc))el)"

Output: "leetcode"

Explanation: First, we reverse the substring "oc", then "etco", and finally,
the whole string.

Constraints:

- 1 <= s.length <= 2000
- s only contains lower case English characters and parentheses.
- It is guaranteed that all parentheses are balanced.
"""

"""
Discussion and examples:
- 'abcd' => no parentheses, so just as is 'abcd'
- '(abcd)' => single set of parentheses, so reversed 'dcba'
- '((abcd))' => logically, if we were to work from inner to outer, it would
  look something like '(bcda)' then 'abcd'
  - observation -- when we find a matching set of parentheses, can we reverse
    the string within, but then leave out the parentheses? e.g.

  - '((abcd))' => '(bcda)'

  - looks like we have to, otherwise we'll have a difficult time tracking
    groups that have flipped with groups that have nto

"""
class Solution:
    """
    >>> s = Solution()
    >>> s.reverseParentheses('(abcd)')
    'dcba'
    >>> s.reverseParentheses('(a(bc)d)')
    'dbca'
    """
    def reverseParentheses(self, s: str) -> str:
        return self.reverseParenthesesStack(s)

    def reverseParenthesesStack(self, s: str) -> str:
        """
        Stack-based solution.
        - Push characters in stack until a close parenthesis is encountered.
        - When a close parenthesis is encountered, use a deque to collect
          (append to end) elements from the stack (pop) until an open
          parenthesis is encountered (should be the matching one). Then,
          insert (pop from front) elements in the deque back into the stack
          (append) -- this effectively does the "reverse" operation.

        Time: O(n^2)
        - O(n) to scan forward for close paren
        - O(n) to scan backward (pop from stack) until matching open paren,
          for each forward scan
        - => O(n^2)

        Space: O(n)
        - O(n) for the stack and deque space
        """
        stk = []
        for c in s:
            if c != ')':
                stk.append(c)
            else:
                values = deque()
                while stk[-1] != '(':
                    values.append(stk.pop())
                stk.pop()
                while len(values) > 0:
                    stk.append(values.popleft())
            # print(stk)
        return ''.join(stk)
        
    def reverseParenthesesNaive(self, s: str) -> str:
        """
        Naive solution that takes care of the purely nested case, but doesn't
        handle serial/consecutive parenthetical statements.

        Strategy -- creep in from both ends, finding matching parentheses,
        and reverse the portion of the string between each parentheses pair.

        Time: O(n) for the scan, O(n) for each reversal during scan, so
        total would be O(n^2)

        Space:
        - O(n) for the aux character array to make it easier to reverse
          rather than doing string reversal and reassembly
        """
        chars = [c for c in s]
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and chars[i] != '(':
                i += 1
            while i < j and chars[j] != ')':
                j -= 1
            i += 1
            j -= 1
            self.reverse(chars, i, j)
            # print(f"i={i},j={j},chars={''.join(chars)}")
        result = []
        for c in chars:
            if c == '(' or c == ')':
                continue
            else:
                result.append(c)
        return ''.join(result)

    def reverse(self, chars: list[str], i: int, j: int) -> None:
        """
        Reverses elements in 'chars' from i to j (inclusive of both)
        """
        m = i
        n = j
        while m < n:
            tmp = chars[m]
            chars[m] = self.flipChar(chars[n])
            chars[n] = self.flipChar(tmp)
            m += 1
            n -= 1

    def flipChar(self, c: str) -> str:
        if c == '(':
            return ')'
        elif c == ')':
            return '('
        else:
            return c

if __name__ == '__main__':
    import doctest
    doctest.testmod()

