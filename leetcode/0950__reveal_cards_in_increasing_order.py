from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> s.deckRevealedIncreasing([17,13,11,2,3,5,7])
        [2, 13, 3, 11, 5, 17, 7]
        >>> s.deckRevealedIncreasing([1, 1000])
        [1, 1000]
        """
        return self.deckRevealedIncreasingSim2(deck)

    def deckRevealedIncreasingSim(self, deck: list[int]) -> list[int]:
        """
        Simulation solution -- simulate the operations, but in reverse

        What are the reversed operations?
        1. Take bottom card and put it on top
        2. Push discarded card on the top

        Time:
        - let n = len(deck)
        - O(n*lg(n)) to create reverse-sorted expected deck
        - O(n) to process each card in the original deck
        - for each card, O(n) to do the shuffle of the unrevealed card
        - O(n) to create list from deque
        - => O(n^2)

        Space:
        - let n = len(deck)
        - => O(n) sorted expected deck
        """
        # start with sorted list - in reverse because we're reversing
        # the entire simulation, so we need to start with the last
        # card we want to reveal, which is the largest card
        expectedDeck = sorted(deck, reverse = True)
        finalDeck = []
        for card in expectedDeck:
            if len(finalDeck) > 0:
                tmpCard = finalDeck.pop()
                finalDeck.insert(0, tmpCard)
            finalDeck.insert(0, card)
        return finalDeck
    
    def deckRevealedIncreasingSim2(self, deck: list[int]) -> list[int]:
        """
        Slight optimization of the above -- use a deque instead of a simple
        list, to improve head/tail insert/remove operatinos

        Time:
        - O(n*lg(n)) reverse sorted expected deck
        - O(n) to process each card in expected deck
        - For each card, O(1) to shuffle end card and "undiscard" the current card
        - O(n) to convert deque to list
        - => O(n*lg(n)) for sufficiently large n

        Space:
        - => O(n) sorted expected deck
        """
        expectedDeck = sorted(deck, reverse = True)
        finalDeck = deque()
        for card in expectedDeck:
            if len(finalDeck) > 0:
                tmpCard = finalDeck.pop()
                finalDeck.appendleft(tmpCard)
            finalDeck.appendleft(card)
        return list(finalDeck)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
