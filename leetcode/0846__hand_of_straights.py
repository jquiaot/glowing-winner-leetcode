from typing import List

import logging
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        >>> s = Solution()
        >>> s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
        True
        >>> s.isNStraightHand([1, 2, 3, 4, 5], 4)
        False
        >>> s.isNStraightHand([1, 1, 2, 2, 3, 3], 3)
        True
        """
        return self.isNStraightHand2(hand, groupSize)

    def isNStraightHand1(self, hand: list[int], groupSize: int) -> bool:
        """
        Object-oriented solution. Still fails on large data sets, so needs
        some improvements.
        """
        hand.sort()
        logger.info(hand)
        d = Dealer(groupSize)
        for card in hand:
            if d.deal(card):
                logger.info(f"Successfully consumed {card}")
                pass
            else:
                logger.info(f"Failed on {card}")
                return False
        return d.isValidDeal()

    def isNStraightHand2(self, hand: list[int], groupSize: int) -> bool:
        """
        """

        # short-circuit check that we can partition hand into groups containing
        # groupSize cards
        if len(hand) % groupSize != 0:
            return False

        # count number of each card in hand
        cardCount = {}
        for card in hand:
            if card not in cardCount:
                cardCount[card] = 1
            else:
                cardCount[card] += 1

        # get unique cards
        uniqueCards = sorted(cardCount.keys())

        for card in uniqueCards:
            while cardCount[card] > 0:
                if not self.mkGroup(cardCount, groupSize, card):
                    return False
        return True

    def mkGroup(self, cardCount: dict[int, int], groupSize: int, card: int) -> bool:
        for i in range(card, card + groupSize):
            if i not in cardCount:
                return False
            elif cardCount[i] == 0:
                return False
            else:
                cardCount[i] -= 1
        return True

class Group:
    def __init__(self, groupSize: int):
        self.cards = []
        self.groupSize = groupSize
    def isComplete(self) -> bool:
        return len(self.cards) == self.groupSize
    def canAccept(self, card: int) -> bool:
        return len(self.cards) == 0 or self.cards[-1] + 1 == card
    def accept(self, card: int) -> None:
        self.cards.append(card)

class Dealer:
    def __init__(self, groupSize: int):
        self.groups = []
        self.groupSize = groupSize

    def deal(self, card: int) -> bool:
        if len(self.groups) == 0:
            logger.info(f"Creating new group with card {card}")
            # create new group
            g = Group(self.groupSize)
            g.accept(card)
            if not g.isComplete():
                self.groups.append(g)
            return True
        else:
            cardAccepted = False
            groupToRemove = None
            for group in self.groups:
                if group.canAccept(card):
                    logger.info(f"Adding card {card} to group {group.cards}")
                    group.accept(card)
                    cardAccepted = True
                    logger.info(f"cardAccepted? {cardAccepted}")
                    if group.isComplete():
                        groupToRemove = group
                    break
            if not cardAccepted:
                logger.info(f"Card {card} not accepted in existing group, creating new")
                g = Group(self.groupSize)
                g.accept(card)
                if not g.isComplete():
                    self.groups.append(g)
            if groupToRemove is not None:
                self.groups.remove(groupToRemove)
            return True

    def isValidDeal(self):
        for group in self.groups:
            if not group.isComplete():
                logger.info(f"Found incomplete group {group.cards}")
                return False
        logger.info("All groups complete, this is valid deal")
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
