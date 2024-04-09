from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        >>> s = Solution()
        >>> s.timeRequiredToBuy([2, 3, 2], 2)
        6
        >>> s.timeRequiredToBuy([5, 1, 1, 1], 0)
        8
        """
        return self.timeRequiredToBuy2(tickets, k)
    
    def timeRequiredToBuy1(self, tickets: list[int], k: int) -> int:
        """
        (Naive) solution - simulate the ticket buying process

        Time:
        - let n = len(tickets)
        - => O(n * k) for the at most k times to run through the list of tickets

        Space:
        - => O(1) to maintain accumulated time
        """
        t = 0
        while True:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    t += 1
                if i == k and tickets[k] == 0:
                    break
            if tickets[k] == 0:
                break
        return t

    def timeRequiredToBuy2(self, tickets: list[int], k: int) -> int:
        """
        Calculation solution:
        - People from k+1 to len(tickets)-1 will contribute min(tickets[k] - 1, tickets[i]) to the time
        - People from 0 to k will contribute min(tickets[k], tickets[i]) to the time

        Time:
        - let n = len(tickets)
        => O(n) to calculate each person's contribution to elapsed time

        Space:
        => O(1) for elapsed time storage
        """
        t = 0
        tickets_k = tickets[k]
        for i in range(k + 1):
            t += min(tickets_k, tickets[i])
        tickets_k_minus_one = tickets_k - 1
        for i in range(k + 1, len(tickets)):
            t += min(tickets_k_minus_one, tickets[i])
        return t

if __name__ == '__main__':
    import doctest
    doctest.testmod()
