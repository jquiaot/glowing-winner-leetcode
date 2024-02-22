from typing import List

"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of
these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the
person labeled ai trusts the person labeled bi. If a trust relationship does
not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be
identified, or return -1 otherwise.

Discussion:

From #1, the town judge will not have a trust entry in the trust list. So
if we maintain a set of people that trust someone, then the town judge
should not appear in that set.

From #2, if we maintain a dict of people that are trusted by others, and
their counts, then

- The set of people who are trusted minus the trusting people should be
  one
- The count of people trusting the one above should be (n - 1)

From #3, the set of trusted people should equal 1, and that person should
not be in trusting people.

Edge case: If there is only one person in town, the trust list should be
empty, and the judge is 1

"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        >>> s = Solution()
        >>> s.findJudge(2, [[1, 2]])
        2
        >>> s.findJudge(3, [[1, 3], [2, 3]])
        3
        >>> s.findJudge(3, [[1, 3], [2, 3], [3, 1]])
        -1
        >>> s.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4]])
        -1
        >>> s.findJudge(3, [[1, 2], [2, 3]])
        -1
        """

        if len(trust) == 0:
            if n == 1:
                # only one person, and no trust records, so this must be the judge
                return 1
            else:
                # more than one person, but no trust records, so there must be
                # no judge that can be identified
                return -1

        trustingPeople = set()
        trustedPeople = {}
        for trustRecord in trust:
            trustingPeople.add(trustRecord[0])
            if trustRecord[1] not in trustedPeople:
                trustedPeople[trustRecord[1]] = 1
            else:
                trustedPeople[trustRecord[1]] += 1

        potentialJudges = set(trustedPeople.keys()).difference(trustingPeople)
        lenPotentialJudges = len(potentialJudges)
        if lenPotentialJudges != 1:
            return -1
        potentialJudge = potentialJudges.pop()
        if trustedPeople[potentialJudge] == (n - 1):
            return potentialJudge
        else:
            return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
