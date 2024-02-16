from typing import List

"""
Given an array of integers arr and an integer k. Find the least number of
unique integers after removing exactly k elements.

Discussion:

We can count the number of occurrences of each element in arr, and then remove
k elements starting with the least unique ones (from lowest number of
occurrences to highest).

Time:
- O(n) to traverse arr and populate dict()
  - O(1) dict lookup and increment
- At most O(n) to remove k elements from arr
- => O(n)

Space:
- => O(n) for dict() storage and array for sorting
"""
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        >>> s = Solution()
        >>> s.findLeastNumOfUniqueInts([5, 5, 4], 1)
        1
        >>> s.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3)
        2
        >>> s.findLeastNumOfUniqueInts([1, 2, 3, 4, 5, 6], 4)
        2
        """
        m = {}
        for i in arr:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        # print(m)

        elts = [ [k, v] for k,v in m.items() ]
        elts.sort(key = lambda x: x[1])
        # print(elts)

        numToRemove = k
        i = 0
        while numToRemove > 0:
            e = elts[i]
            if e[1] > numToRemove:
                e[1] -= numToRemove
                numToRemove = 0
            else:
                # print(f"trying to remove {e} from {m}")
                numToRemove -= e[1]
                del m[e[0]]
            i += 1

        return len(m)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
