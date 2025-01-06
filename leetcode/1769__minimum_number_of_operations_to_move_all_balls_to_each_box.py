from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        >>> s = Solution()
        >>> s.minOperations('110')
        [1, 1, 3]
        >>> s.minOperations('001011')
        [11, 8, 5, 4, 3, 4]
        """
        return self.minOperations1(boxes)

    def minOperations1(self, boxes: str) -> List[int]:
        """
        - Accumulate steps in both directions (l->r, r->l)
          - If boxes[i] == '1', then start accumulating at i+1
        - Steps then combine to for answer
        '001011'
        left to right accum: [0, 0, 0, 1, 2, 4]
        right to left accum: [11, 8, 5, 3, 1, 0]
        sum: [11, 8, 5, 4, 3, 4]
        """
        answer = [0 for c in boxes]
        answerLR = [0 for c in boxes]
        answerRL = [0 for c in boxes]

        cumulativeSum = int(boxes[0])
        for i in range(1, len(boxes)):
            answerLR[i] = answerLR[i - 1] + cumulativeSum
            cumulativeSum += int(boxes[i])

        cumulativeSum = int(boxes[-1])
        for i in range(len(boxes) - 2, -1, -1):
            answerRL[i] = answerRL[i + 1] + cumulativeSum
            cumulativeSum += int(boxes[i])

        for i in range(len(answer)):
            answer[i] = answerLR[i] + answerRL[i]
        return answer

if __name__ == '__main__':
    import doctest
    doctest.testmod()
