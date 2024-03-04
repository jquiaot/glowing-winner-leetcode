import logging
from typing import List

logging.basicConfig(level = logging.DEBUG)

"""
You start with an initial power of power, an initial score of 0, and a bag of
tokens given as an integer array tokens, where each tokens[i] donates the value
of tokeni.

Your goal is to maximize the total score by strategically playing these
tokens. In one move, you can play an unplayed token in one of the two ways (but
not both for the same token):

- Face-up: If your current power is at least tokens[i], you may play tokeni,
    losing tokens[i] power and gaining 1 score.

- Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.

Return the maximum possible score you can achieve after playing any number of
tokens.

Example 1:

Input: tokens = [100], power = 50

Output: 0

Explanation: Since your score is 0 initially, you cannot play the token
face-down. You also cannot play it face-up since your power (50) is less than
tokens[0] (100).

Example 2:

Input: tokens = [200,100], power = 150

Output: 1

Explanation: Play token1 (100) face-up, reducing your power to 50 and
increasing your score to 1.

There is no need to play token0, since you cannot play it face-up to add to
your score. The maximum score achievable is 1.

Example 3:

Input: tokens = [100,200,300,400], power = 200

Output: 2

Explanation: Play the tokens in this order to get a score of 2:

1. Play token0 (100) face-up, reducing power to 100 and increasing score to 1.

2. Play token3 (400) face-down, increasing power to 500 and reducing score to 0.

3. Play token1 (200) face-up, reducing power to 300 and increasing score to 1.

4. Play token2 (300) face-up, reducing power to 0 and increasing score to 2.

The maximum score achievable is 2.
"""
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        Doctest test cases:

        >>> s = Solution()
        >>> s.bagOfTokensScore([33, 4, 28, 24, 96], 35)
        3
        >>> s.bagOfTokensScore([52,65,35,88,28,1,4,68,56,95], 94)
        5
        >>> s.bagOfTokensScore([1,2,3,4], 10)
        4
        >>> s.bagOfTokensScore([100], 50)
        0
        >>> s.bagOfTokensScore([200, 100], 150)
        1
        >>> s.bagOfTokensScore([100, 200, 300, 400], 200)
        2
        """
        # return self.bagOfTokensScoreMemo(sorted(tokens, reverse = True), power, 0)
        return self.bagOfTokensScoreGreedy(sorted(tokens), power)

    """
    Recursively explore the possible solution space.

    At each step, have two choices:
    1. If current power is at least the token value, play a token face-up:
       - Remove token from list
       - Decrease power by token value
       - Increment score by 1
    2. If current score is at least 1, play a token face-down:
       - Remove token from list
       - Increase power by token value
       - Decrement score by 1

    Base cases to track:
    - tokens is empty -- no more moves, return score

    Time:
    - Given n = len(tokens)
    - Given m = score
    - Basically constructing a tree of all possible plays
    - Max height of tree == O(m) (think all tokens are 1's)
    - Branching factor == O(n)
    - At each level, copying tokens for recursive step == O(m)
    - => O(n^m * m)

    Space:
    - Given n = len(tokens)
    - Given m = score
    - Again, height of tree == O(m)
    - Storage at each level == O(m) for list of nodes
    - => O(m^2)
    """
    def bagOfTokensScoreRecur(self, tokens: list[int], power: int, score: int) -> int:
        logging.debug(f"exploring tokens={tokens}, power={power}, score={score}")
        if len(tokens) == 0:
            logging.debug(f"No more tokens, returning score={score}")
            return score
        else:
            # for each token remaining in tokens, recursively explore playing
            # token face-up or face-down (if possible in either scenario), and
            # keeping track of the best score encountered
            bestScore = score
            for token in tokens:
                logging.debug(f"Trying token={token}")
                if power >= token:
                    logging.debug("Trying face-up")
                    newTokens = [*tokens]
                    newTokens.remove(token)
                    newPower = power - token
                    newScore  = score + 1
                    possibleScore = self.bagOfTokensScoreRecur(newTokens, newPower, newScore)
                    if possibleScore > bestScore:
                        bestScore = possibleScore
                else:
                    logging.debug("Can't try face-up")
                    pass
                if score > 0:
                    logging.debug("Trying face-down")
                    newTokens = [*tokens]
                    newTokens.remove(token)
                    newPower = power + token
                    newScore  = score - 1
                    possibleScore = self.bagOfTokensScoreRecur(newTokens, newPower, newScore)
                    if possibleScore > bestScore:
                        bestScore = possibleScore
                else:
                    logging.debug("Can't try face-down")
                    pass
            logging.debug(f"tokens={tokens} => bestScore={bestScore}")
            return bestScore

    """
    Memoized version of above.

    What do we need to memoize? Stringified version of the remaining tokens to optimal
    score for those tokens. That way we don't retry that combination of tokens.

    Need an additional step of sorting the tokens before entering here, so that
    we can generate a consistent hash string.
    """
    def bagOfTokensScoreMemo(self, tokens: list[int], power: int, score: int, memo: dict[str, int] = None) -> int:
        logging.debug(f"exploring tokens={tokens}, power={power}, score={score}")
        if len(tokens) == 0:
            logging.debug(f"No more tokens, returning score={score}")
            return score
        if memo is None:
            memo = {}
        key = ','.join(map(str, tokens))
        if key in memo:
            return memo[key]
        else:
            # for each token remaining in tokens, recursively explore playing
            # token face-up or face-down (if possible in either scenario), and
            # keeping track of the best score encountered
            bestScore = score
            for token in tokens:
                logging.debug(f"Trying token={token}")
                if power >= token:
                    logging.debug("Trying face-up")
                    newTokens = self.arrayCopy(tokens, token)
                    newPower = power - token
                    newScore  = score + 1
                    possibleScore = self.bagOfTokensScoreMemo(newTokens, newPower, newScore)
                    if possibleScore > bestScore:
                        bestScore = possibleScore
                if score > 0:
                    logging.debug("Trying face-down")
                    newTokens = self.arrayCopy(tokens, token)
                    newPower = power + token
                    newScore  = score - 1
                    possibleScore = self.bagOfTokensScoreMemo(newTokens, newPower, newScore)
                    if possibleScore > bestScore:
                        bestScore = possibleScore
            logging.debug(f"tokens={tokens} => bestScore={bestScore}")
            memo[key] = bestScore
            return bestScore

    def arrayCopy(self, a: list[int], b: int) -> list[int]:
        l = []
        removed = False
        for i in a:
            if not removed and i == b:
                removed = True
                continue
            else:
                l.append(i)
        return l

    """
    Greedy approach as suggested by discussion:
    - Sort list
    - Maintain two pointers, one at start, one at end
    - Earn points from front of list (cheapest points)
    - Add power from end of list (largest amount of power)
    - Break if we run out of tokens or we have no more moves that can earn
      us points

    Time:
    - n = len(tokens)
    - => O(n) traverse list of tokens at most once
    Space:
    - => O(1) constant space to store the score and current power
    """
    def bagOfTokensScoreGreedy(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        score = 0
        curPower = power
        i = 0
        j = len(tokens) - 1
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                i += 1
                score += 1
            elif score > 0 and i < j:
                    power += tokens[j]
                    j -= 1
                    score -= 1
                    power -= tokens[i]
                    i += 1
                    score += 1
            else:
                # no more valid moves to make
                break
        return score

if __name__ == '__main__':
    import doctest
    doctest.testmod()
