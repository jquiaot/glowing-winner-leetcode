OPEN_BRACKETS = {'(', '{', '['}

CLOSED_BRACKET_MAP = {
    ')': '(',
    '}': '{',
    ']': '['
}

class Solution:
    def isValid(self, s: str) -> bool:
        """
        When encountering an open bracket, push bracket onto stack.

        When encountering a close bracket, check that the bracket at top of
        stack is the corresponding open bracket type. If it is, pop it, else
        it's an invalid string.

        If we've consumed the entire string and the stack is empty, then it's
        a valid string.

        Time:
        - O(n) for n = len(s) to traverse string s
        - set and dict key lookups, which are O(1)
        - => O(n)

        Space:
        - => O(1) some static data structures to match up brackets

        >>> s = Solution()
        >>> s.isValid("()")
        True
        >>> s.isValid("()[]{}")
        True
        >>> s.isValid("(]")
        False
        >>> s.isValid("]")
        False
        >>> s.isValid("({[)}]")
        False
        >>> s.isValid("(({}[]))")
        True
        """
        stk = [] # use a list as stack, we'll just use append()/pop()

        for c in s:
            if c in OPEN_BRACKETS:
                stk.append(c)
            elif len(stk) == 0:
                # empty stack and closed bracket - no corresponding open, so
                # invalid string
                return False
            else:

                t = stk.pop()
                # print(f"t={t}, c={c}, CLOSED_BRACKET_MAP['{c}'] = {CLOSED_BRACKET_MAP[c]}")
                if t != CLOSED_BRACKET_MAP[c]:
                    return False
        
        return len(stk) == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()

