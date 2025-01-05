from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        >>> s = Solution()
        >>> s.shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]])
        'ace'
        >>> s.shiftingLetters("dztz", [[0,0,0],[1,1,1]])
        'catz'
        """
        return self.shiftingLetters2(s, shifts)
 
    def shiftingLetters1(self, s: str, shifts: List[List[int]]) -> str:
        """
        - Maintain a list of shifts for each character in s
        - For each shift, apply to the above list
        - After all shifts are calculated, figure out for each char
          what the final character should be, based on list of shifts
        """

        charShifts = [0 for c in s]

        for shift in shifts:
            shiftDir = 1 if shift[2] == 1 else -1
            for i in range(shift[0], shift[1] + 1):
                charShifts[i] += shiftDir

        chars = [c for c in 'abcdefghijklmnopqrstuvwxyz']
        ordA = ord('a')
        newS = []
        for i in range(len(s)):
            c = s[i]
            newC = chars[(ord(c) - ordA + charShifts[i]) % 26]
            newS.append(newC)
        return ''.join(newS)

    def shiftingLetters2(self, s: str, shifts: List[List[int]]) -> str:
        """
        Using hints: similar to above, but somehow setup prefix sum to
        manage the offsets
        """
        charShifts = [0 for c in s]
        maxIdx = len(s) - 1
        for shift in shifts:
            shiftDir = 1 if shift[2] == 1 else -1
            charShifts[shift[0]] += shiftDir
            if shift[1] < maxIdx:
                charShifts[shift[1] + 1] -= shiftDir

        chars = [c for c in 'abcdefghijklmnopqrstuvwxyz']
        ordA = ord('a')
        newS = []
        curOffset = 0
        for i in range(len(s)):
            c = s[i]
            curOffset += charShifts[i]
            newC = chars[(ord(c) - ordA + curOffset) % 26]
            newS.append(newC)
        return ''.join(newS)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
