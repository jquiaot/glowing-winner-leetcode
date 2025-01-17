from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        >>> s = Solution()
        >>> s.doesValidArrayExist([1, 1, 0])
        True
        >>> s.doesValidArrayExist([1, 1])
        True
        >>> s.doesValidArrayExist([1, 0])
        False
        """
        return self.doesValidArrayExist1(derived)

    def doesValidArrayExist1(self, derived: list[int]) -> bool:
        """
        derived = [d0, d1]
        o0 ^ o1 = d0
        o1 ^ o0 = d1

        derived = [d0, d1, d2]
        o0 ^ o1 = d0
        o1 ^ o2 = d1
        o2 ^ o0 = d2

        derived = [d0, d1, d2, ..., dn]
        o0 ^ o1 = d0
        o1 ^ o2 = d1
        o2 ^ o3 = d2
        ...
        on ^ o0 = dn

        Observation (also from hint): Each original element appears twice.

        The XOR of all derived elements should equal the XOR of the
        original elements twice.

        Since we're XORing all the original elements twice, they should
        cancel each other out, so the result should be 0.

        So we just need to test that the XOR of all derived elements equals 0.

        Time:
        - n = len(derived)
        - => O(n) iterate through derived to calculate XOR of all elements
        
        Space:
        - n = len(derived)
        - O(1) aux space to store the accumulated XOR value
        """
        xorValue = 0
        for i in derived:
            xorValue ^= i
        return xorValue == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
