"""
You are given two strings order and s. All the characters of order are unique
and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was
sorted. More specifically, if a character x occurs before a character y in
order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Example 1:

Input: order = "cba", s = "abcd"

Output: "cbad"

Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c"
should be "c", "b", and "a".

Since "d" does not appear in order, it can be at any position in the returned
string. "dcba", "cdba", "cbda" are also valid outputs.

Example 2:

Input: order = "bcafg", s = "abcd"

Output: "bcad"

Explanation: The characters "b", "c", and "a" from order dictate the order for
the characters in s. The character "d" in s does not appear in order, so its
position is flexible.

Following the order of appearance in order, "b", "c", and "a" from s should be
arranged as "b", "c", "a". "d" can be placed at any position since it's not in
order. The output "bcad" correctly follows this rule. Other arrangements like
"bacd" or "bcda" would also be valid, as long as "b", "c", "a" maintain their
order.
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        >>> s = Solution()
        >>> s.customSortString("cba", "abcd")
        'cbad'
        >>> s.customSortString("bcafg", "abcd")
        'bcad'
        """
        return self.customSortString1(order, s)

    def customSortString1(self, order: str, s: str) -> str:
        """
        1. Create a dictionary from char in 'order' to number of occurrences of that char in 's'
        2. Create a list to collect characters not in 'order'
        3. Iterate through s.
           - Encounter char in 'order'? Count it in dict
           - Not in 'order'? Add it to list of others
        4. Using 'order', build array of chars from 'order' according to number found in 's'
        5. Finally join others to this 'order' list
        6. Join all chars

        Time:
        - m = len(order)
        - n = len(s)
        - O(m) to initialize orderChars dict
        - O(n) to see all chars in s and either add count to orderChars or append char to restOfChars
        - O(n) to assemble final list
        - O(n) to generate final string
        - => O(m + n)

        Space:
        - m = len(order)
        - n = len(s)
        - O(m) dict of chars in order
        - O(n) for rest of chars
        - O(n) final string list
        - => O(m + n)
        """
        orderChars = {}
        restOfChars = []
        for c in order:
            orderChars[c] = 0
        
        for c in s:
            if c in orderChars:
                orderChars[c] += 1
            else:
                restOfChars.append(c)
        
        finalStringList = []
        for c in order:
            for i in range(orderChars[c]):
                finalStringList.append(c)
        if len(restOfChars) > 0:
            finalStringList.extend(restOfChars)
        
        return ''.join(finalStringList)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
