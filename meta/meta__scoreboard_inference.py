from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    """
    Discussion: So apparently, we have two cases we need to consider:
    
    1. There is an odd-numbered score 2. There is no odd-numbered score
    
    We'll take #2 first. If there is no odd-numbered score (i.e., all scores
    are even), then the minimum number of problems we need is the greatest
    score divided by 2.
    
    If there is at least one odd-numbered score, then we need at least one
    1-point question in order to be able to construct all scores. The number of
    2-point questions the is half of (max score - 2) -- if we have 2 1-point
    questions, we can use that to construct an even score. Even if we have 1
    1-point question, that should still work -- 1 1-point question,
    1+(maxScore-2)//2 2-point questions because we need to make the max score
    somehow.

    >>> getMinProblemCount(6, [1, 2, 3, 4, 5, 6])
    4
    >>> getMinProblemCount(4, [4, 3, 3, 4])
    3
    >>> getMinProblemCount(4, [2, 4, 6, 8])
    4
    """
    maxScore = 0
    hasOdd = False
    for x in S:
        if x % 2 == 1:
            hasOdd = True
        if maxScore < x:
            maxScore = x
    if hasOdd:
        return 2 + (maxScore - 2) // 2
    else:
        return maxScore // 2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
