from typing import List
from collections import deque

"""
There are NN dishes in a row on a kaiten belt, with the iith dish being of
type DiDi​. Some dishes may be of the same type as one another.

You're very hungry, but you'd also like to keep things interesting. The NN
dishes will arrive in front of you, one after another in order, and for each
one you'll eat it as long as it isn't the same type as any of the previous KK
dishes you've eaten. You eat very fast, so you can consume a dish before the
next one gets to you. Any dishes you choose not to eat as they pass will be
eaten by others.

Determine how many dishes you'll end up eating.

Please take care to write a solution which runs within the time limit.
"""
def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    """
    >>> getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 1)
    5
    >>> getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 2)
    4
    >>> getMaximumEatenDishCount(7, [1, 2, 1, 2, 1, 2, 1], 2)
    2
    """
    return getMaximumEatenDishCount1(N, D, K)

"""
Discussion:

The solution below fails due to time limit exceeded on one test case, passing
32/33 test cases.

Approach is to use both a set and a deque to keep track of the
last K dishes eaten. The set is for fast lookup of whether we've eaten
a candidate dish. The deque is for maintaining an ordered list
of the dishes eaten, so once we get to K dishes eaten and we're going to
eat a new one, we can know which dish to remove from the set of eaten
dishes.
"""
def getMaximumEatenDishCount1(N: int, D: List[int], K: int) -> int:
    dishCount = 0

    # use a set to have O(1) lookup of whether we've seen the current dish
    # use a dequee to keep track of the K dishes we've seen, and to know
    # which one we need to drop when we're ready to eat a new one

    d = DishTracker(K)
    
    for curDish in D:
        # if we've eaten fewer dishes than the K we need to keep track of,
        # just eat the curDish and add it to the set and queue
        # curEatenCount = d.eat(curDish)
        # print(f"Ate {curDish}? {curEatenCount == 1}")
        # dishCount += curEatenCount
        dishCount += d.eat(curDish)
    return dishCount

"""
Class to keep track of dishes eaten. Supports two methods:
- canEat(dish) - whether or not we've eaten the specified dish
- eat(dish) - eat the specified dish, and remove the dish eaten least recently
"""
class DishTracker:
    def __init__(self, maxDishes: int):
        self.eatenSet = set()
        self.eatenQueue = deque()
        self.maxDishes = maxDishes
        self.curDishes = 0

    def canEat(self, dish: int) -> bool:
        # when can we eat?
        return dish not in self.eatenSet


    def eat(self, dish: int) -> int:
        # print(f"Trying to eat {dish}, already eaten {self.eatenSet}")
        if self.canEat(dish):
            if self.curDishes > 0 and self.curDishes == self.maxDishes:
                lastEaten = self.eatenQueue.popleft()
                self.eatenSet.remove(lastEaten)
                self.curDishes -= 1
            self.eatenSet.add(dish)
            self.eatenQueue.append(dish)
            self.curDishes += 1
            return 1
        else:
            return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
