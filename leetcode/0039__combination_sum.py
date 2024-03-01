from typing import List

"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two
combinations are unique if the frequency of at least one of the chosen numbers
is different.

The test cases are generated such that the number of unique combinations that
sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7

Output: [[2,2,3],[7]]

Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used
multiple times.  7 is a candidate, and 7 = 7.  These are the only two
combinations.

Example 2:

Input: candidates = [2,3,5], target = 8

Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1

Output: []
"""
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        >>> s = Solution()
        >>> s.combinationSum([1, 2], 3)
        [[1, 1, 1], [1, 2]]
        >>> s.combinationSum([2, 3, 6, 7], 7)
        [[2, 2, 3], [7]]
        """
        return self.combinationSumMemo(candidates, target)

    """
    Discussion: We can use a recursive function to build valid combinations
    of candidates. For each recursive step, we will expand on the previous
    combinations with the available candidates.

    Where do we stop?
    - target < 0 => there's no way to pull any value from candidates to sum
      up to a negative number, so we should return None
    - target == 0 => we don't need to pull any value from candidates to
      hit the target, so return a single empty list
    - target > 0 => we recursively explore expanding the

    Time:
    - m = target
    - n = len(candidates)
    - since we're essentially building a tree from the recursions of all possible
      combinations, the height of the tree would be O(m) worse case
    - for each non-leaf node, max number of children would be O(n) (length of candidates),
      because we are attempting to extend combinations with all the candidate values
    - O(n^m) for the recursion - (branching factor n) ^ (height factor m)
    - Need to factor in O(m) for copying over each combination (think all 1's)
    - => O(n^m * m)

    Space:
    - m = target
    - n = len(candiates)
    - height of recursion == O(m)
    - if we only consider extra space on the call stack, it should be O(m * n) ?
    """
    def combinationSumRecur(self, candidates: list[int], target: int) -> list[list[int]]:
        if target < 0:
            return None
        if target == 0:
            return [[]]
        else:
            # build a dict of valid combinations, as a mapping from a string
            # representation of the sorted combination to the combination itself,
            # to allow us to filter out dupes
            combinations = {}
            # for each candidate, get a list of combinations that sum up
            # to the remainder of target - candidate
            for candidate in candidates:
                remainder = target - candidate
                remainderResult = self.combinationSumRecur(candidates, remainder)
                # if the remainderResult is None, then the remainder (target)
                # must have been negative, so just discard, as this is a dead-end
                # otherwise, collect the combinations by extending the
                # remainderResult collections with candidate
                if remainderResult is not None:
                    for resultCombination in remainderResult:
                        extendedCombo = sorted([*resultCombination, candidate])
                        comboKey = ','.join(map(str, extendedCombo))
                        combinations[comboKey] = extendedCombo
            return list(combinations.values())

    """
    Memoized version of the above. First check if the values for target are already generated,
    and if so return it. Otherwise, calculate and save for later.

    Time:
    - => O(m^2 * n)
    Space:
    - => O(m^2) ?
    """
    def combinationSumMemo(self, candidates: list[int], target: int, memo: dict[int, list[list[int]]] = None) -> list[list[int]]:
        if memo is None:
            memo = {}
        key = target
        if key in memo:
            return memo[key]
        if target < 0:
            return None
        if target == 0:
            return [[]]
        else:
            # build a dict of valid combinations, as a mapping from a string
            # representation of the sorted combination to the combination itself,
            # to allow us to filter out dupes
            combinations = {}
            # for each candidate, get a list of combinations that sum up
            # to the remainder of target - candidate
            for candidate in candidates:
                remainder = target - candidate
                remainderResult = self.combinationSumMemo(candidates, remainder, memo)
                # if the remainderResult is None, then the remainder (target)
                # must have been negative, so just discard, as this is a dead-end
                # otherwise, collect the combinations by extending the
                # remainderResult collections with candidate
                if remainderResult is not None:
                    for resultCombination in remainderResult:
                        extendedCombo = sorted([*resultCombination, candidate])
                        comboKey = ','.join(map(str, extendedCombo))
                        combinations[comboKey] = extendedCombo
            memo[key] = list(combinations.values())
            return memo[key]
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
